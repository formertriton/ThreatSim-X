import json
import os
from datetime import datetime

LOG_DIR = "data/logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_incident(alert):
    filename = f"{LOG_DIR}/incident_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(alert, f, indent=2)
    print(f"[LOGGER] Incident logged to {filename}")
