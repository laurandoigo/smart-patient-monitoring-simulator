# simulator/sensors.py
from simulator.patient_model import Patient
import pandas as pd

class SensorSimulator:
    def __init__(self, patients):
        self.patients = patients
        self.history = []
        self.time_step = 0

    def run_step(self):
        """Update all patients and store a step"""
        step_data = []
        for p in self.patients:
            p.update_vitals()
            step_data.append({
                "id": str(p.id),  # string for Plotly color
                "temperature": float(p.temperature),
                "flow_rate": float(p.flow_rate),
                "pressure": float(p.pressure),
                "bubble": bool(p.bubble),
                "time_step": int(self.time_step)
            })

        self.history.append(step_data)
        self.time_step += 1
        return step_data

    def get_history_df(self):
        """Return history as a DataFrame"""
        rows = [record for step in self.history for record in step]
        df = pd.DataFrame(rows)
        return df
