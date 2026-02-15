# dashboard/app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from simulator.patient_model import Patient
from simulator.sensors import SensorSimulator
from simulator.logger import log_data
from simulator.alerts import check_alerts

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="Smart Patient Monitoring Simulator", layout="wide")
st.title("🩺 Smart Patient Monitoring Simulator")

# -----------------------------
# Simulation parameters
# -----------------------------
NUM_PATIENTS = 10
WINDOW_SIZE = 10
STEP_INTERVAL = 1  # minutes per step

# Vital thresholds
TEMP_MIN, TEMP_MAX = 36.0, 38.0
PRESSURE_MIN, PRESSURE_MAX = 90, 125
FLOW_MIN, FLOW_MAX = 3.0, 6.0

# -----------------------------
# Initialize patients and simulator
# -----------------------------
if "patients" not in st.session_state or len(st.session_state.patients) != NUM_PATIENTS:
    st.session_state.patients = [Patient(id=i) for i in range(1, NUM_PATIENTS + 1)]
if "simulator" not in st.session_state:
    st.session_state.simulator = SensorSimulator(st.session_state.patients)

sim = st.session_state.simulator

# -----------------------------
# Pre-fill initial steps so lines appear immediately
# -----------------------------
if "simulator_initialized" not in st.session_state:
    for _ in range(WINDOW_SIZE):
        sim.run_step()
    st.session_state.simulator_initialized = True

# -----------------------------
# Run Step button
# -----------------------------
if st.button("Run Step"):
    data = sim.run_step()
    log_data(data)

    df = pd.DataFrame(data)

    # -----------------------------
    # Alerts
    # -----------------------------
    alerts = check_alerts(
        data,
        temp_min=TEMP_MIN,
        temp_max=TEMP_MAX,
        pressure_min=PRESSURE_MIN,
        pressure_max=PRESSURE_MAX,
        flow_min=FLOW_MIN,
        flow_max=FLOW_MAX
    )

    # -----------------------------
    # Display table
    # -----------------------------
    st.subheader("Patient Data (Latest Step)")
    st.dataframe(df.drop(columns=["time_step"]).style.format({
        "temperature": "{:.1f} °C",
        "flow_rate": "{:.1f} mL/min",
        "pressure": "{:.0f} mmHg"
    }))

    # -----------------------------
    # Display alerts
    # -----------------------------
    st.subheader("🚨 Alerts")
    if alerts:
        for alert in alerts:
            st.warning(f"Patient {alert[0]}: {alert[1]}")
    else:
        st.success("✅ No alerts")

# -----------------------------
# Plot trends
# -----------------------------
st.subheader(f"📊 Vital Trends (Last {WINDOW_SIZE} Steps)")
history_df = sim.get_history_df()
if not history_df.empty:
    history_df['Time (min)'] = history_df['time_step'] * STEP_INTERVAL
    max_step = history_df['time_step'].max()
    start_step = max(0, max_step - WINDOW_SIZE + 1)
    recent_history = history_df[history_df['time_step'] >= start_step].copy()

    def plot_vital(y_col, y_min, y_max, title):
        fig = go.Figure()
        for pid in sorted(recent_history['id'].unique()):
            patient_data = recent_history[recent_history['id'] == pid].sort_values(by='Time (min)')
            fig.add_trace(go.Scatter(
                x=patient_data['Time (min)'],
                y=patient_data[y_col],
                mode='lines+markers',
                name=f"Patient {pid}"
            ))
        # Threshold lines
        fig.add_hline(y=y_max, line_dash="dash", line_color="red",
                      annotation_text=f"{title} Max", annotation_position="top right")
        fig.add_hline(y=y_min, line_dash="dash", line_color="green",
                      annotation_text=f"{title} Min", annotation_position="bottom right")
        fig.update_layout(title=title, xaxis_title="Time (min)", yaxis_title=title)
        return fig

    st.plotly_chart(plot_vital("temperature", TEMP_MIN, TEMP_MAX, "Temperature (°C)"), use_container_width=True)
    st.plotly_chart(plot_vital("pressure", PRESSURE_MIN, PRESSURE_MAX, "Pressure (mmHg)"), use_container_width=True)
    st.plotly_chart(plot_vital("flow_rate", FLOW_MIN, FLOW_MAX, "Flow Rate (mL/min)"), use_container_width=True)
