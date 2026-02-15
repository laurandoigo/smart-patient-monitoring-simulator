# simulator/patient_model.py

import random

class Patient:
    def __init__(self, id):
        self.id = id
        self.temperature = 37.0
        self.flow_rate = 5.0
        self.pressure = 120.0
        self.bubble = False
        self.temp_drift = random.uniform(-0.05, 0.05)  # gradual drift
        self.flow_drift = random.uniform(-0.05, 0.05)
        self.pressure_drift = random.uniform(-0.2, 0.2)

    def update_vitals(self):
        """Simulate vitals with random variation and gradual drift"""
        self.temperature += random.uniform(-0.2, 0.2) + self.temp_drift
        self.flow_rate += random.uniform(-0.5, 0.5) + self.flow_drift
        self.pressure += random.uniform(-2, 2) + self.pressure_drift

        # Rare bubble events (0.5% chance)
        self.bubble = random.random() < 0.005
