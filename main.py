import time
from simulators.brute_force import simulate_brute_force
from detectors.anomaly_detector import detect_brute_force
from responders.block_ip import block_ip
from responders.logger import log_incident
from responders.notify_admin import notify_admin

def main():
    print("Starting ThreatSim Framework...")

    attacks = simulate_brute_force(target_ip="127.0.0.1", attempts=50)
    print(f"Total simulated attacks: {len(attacks)}")

    # Show first 5 attacks for debugging
    for attack in attacks[:5]:
        print(attack)

    alerts = detect_brute_force(attacks, threshold=20)
    print(f"Detected alerts: {len(alerts)}")

    for alert in alerts:
        print(f"Alert: {alert}")
        block_ip(alert['source_ip'])
        log_incident(alert)
        notify_admin(alert)

    print("Simulation complete.")

if __name__ == "__main__":
    main()
