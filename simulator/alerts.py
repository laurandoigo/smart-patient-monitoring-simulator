# simulator/alerts.py

def check_alerts(patient_data, temp_min=36.0, temp_max=38.0,
                 pressure_min=90, pressure_max=125,
                 flow_min=3.0, flow_max=6.0):
    """
    Check patient data for threshold violations and bubble detection.

    Parameters:
    - patient_data: list of dicts, each dict contains sensor readings for a patient
    - temp_min, temp_max: temperature thresholds (°C)
    - pressure_min, pressure_max: pressure thresholds (mmHg)
    - flow_min, flow_max: flow rate thresholds (mL/min)

    Returns:
    - alerts: list of tuples (patient_id, alert_message)
    """
    alerts = []
    for p in patient_data:
        # Temperature
        if p["temperature"] > temp_max:
            alerts.append((p["id"], f"High temperature {p['temperature']:.1f} °C"))
        elif p["temperature"] < temp_min:
            alerts.append((p["id"], f"Low temperature {p['temperature']:.1f} °C"))

        # Pressure
        if p["pressure"] > pressure_max:
            alerts.append((p["id"], f"High pressure {p['pressure']:.0f} mmHg"))
        elif p["pressure"] < pressure_min:
            alerts.append((p["id"], f"Low pressure {p['pressure']:.0f} mmHg"))

        # Flow rate
        if p["flow_rate"] > flow_max:
            alerts.append((p["id"], f"High flow rate {p['flow_rate']:.1f} mL/min"))
        elif p["flow_rate"] < flow_min:
            alerts.append((p["id"], f"Low flow rate {p['flow_rate']:.1f} mL/min"))

        # Bubble detection
        if p["bubble"]:
            alerts.append((p["id"], f"Bubble detected!"))

    return alerts
