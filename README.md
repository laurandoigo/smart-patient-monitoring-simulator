# 🏥 Smart Patient Monitoring Simulator

## Overview

The Smart Patient Monitoring Simulator is a real-time, multi-patient monitoring system that models hospital bedside devices and physiological sensor behavior. The system simulates temperature, flow rate, pressure, and air-in-line (bubble) detection signals with realistic variability, noise injection, and fault conditions.

This project demonstrates end-to-end systems integration — from physiological modeling and sensor simulation to automated alert logic, structured data logging, and live dashboard visualization.

It showcases skills directly applicable to medical device R&D, systems engineering, verification, and smart hospital monitoring platforms.

---

## Key Features

- Multi-patient simulation with unique physiological baselines  
- Real-time sensor signal generation (temperature, flow, pressure, bubble detection)  
- Noise injection and drift modeling to simulate real sensor behavior  
- Automated alert engine with threshold and rate-of-change detection  
- Fault injection (occlusion, hypothermia, air-in-line events)  
- Structured data logging for traceability  
- Interactive real-time dashboard  
- Modular, scalable architecture  

---

## Engineering Highlights

- Modular architecture separating patient model, sensor layer, alert logic, and visualization  
- Gaussian noise and drift modeling to simulate real-world sensor variability  
- Automated alert confirmation logic to reduce false positives  
- Structured event logging for traceability and post-test analysis  
- Real-time dashboard with live visualization and alert tracking  

---

## Technology Stack

- Python  
- Streamlit  
- NumPy  
- Pandas  
- Plotly  
- SQLite (optional for logging)  

All components use open-source tools and are hosted at zero cost.

---

## System Architecture

```
Patient Model
    ↓
Sensor Simulation
    ↓
Signal Conditioning
    ↓
Alert Engine
    ↓
Data Logger
    ↓
Real-Time Dashboard
```
Each module is **modular and independent**, allowing scalability, testing, and feature expansion.  
The flow represents **real-time patient monitoring**, from physiological modeling to visualization and alerts.

---

## Example Simulated Parameters

| Sensor | Modeled Behavior |
|--------|------------------|
| Temperature | Baseline + circadian drift + Gaussian noise |
| Flow Rate | Pump-controlled step response + variability |
| Pressure | Normal operation + occlusion spike simulation |
| Bubble Detection | Probabilistic rare event injection |

---

## Running Locally

Clone the repository:

```
git clone https://github.com/yourusername/smart-patient-monitoring-simulator.git
cd smart-patient-monitoring-simulator
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the dashboard:

```
streamlit run app.py
```

---

## Deployment

This application can be deployed for free using Streamlit Community Cloud.

1. Go to https://streamlit.io/cloud  
2. Connect your GitHub repository  
3. Select `app.py`  
4. Deploy  

---

## Future Enhancements

- Monte Carlo simulation across 100+ patients  
- FMEA-based risk modeling  
- Alert sensitivity vs specificity analysis  
- Sensor calibration drift modeling  
- Exportable verification-style reports  

---

## Author

**Laura Ndoigo**  
Medical Device R&D | Systems Engineering | Verification & Automation| Informatics
