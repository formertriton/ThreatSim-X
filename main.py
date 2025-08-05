"""
Entry point to run simulations and trigger detection/response
"""
import time
from simulators.brute_force import simulate_brute_force
from detectors.anomaly_detector import detect_brute_force
from responders.block_ip import block_ip
from responders.logger import log_incident
from responders.notify_admin import notify_admin

def main():
    print("Starting ThreatSim Framework...")

    # Simulate brute force attack
    attacks = simulate_brute_force(target_ip="127.0.0.1", attempts=50)

    # Detect attacks
    alerts = detect_brute_force(attacks, threshold=20)

    # Respond to alerts
    for alert in alerts:
        block_ip(alert['source_ip'])
        log_incident(alert)
        notify_admin(alert)

    print("Simulation complete.")

if __name__ == "__main__":
    main()
