import csv
from datetime import datetime
import os

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

def log_data(patient_data, filename="data/log.csv"):
    """Append patient readings to a CSV file"""
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        for p in patient_data:
            writer.writerow([
                datetime.now(),
                p["id"],
                p["temperature"],
                p["flow_rate"],
                p["pressure"],
                p["bubble"]
            ])
