import streamlit as st
import time
from simulators.brute_force import simulate_brute_force
from detectors.anomaly_detector import detect_brute_force

if 'attacks' not in st.session_state:
    st.session_state.attacks = []
if 'alerts' not in st.session_state:
    st.session_state.alerts = []

st.title("ThreatSim-X Dashboard")

def run_simulation():
    new_attacks = simulate_brute_force(target_ip="127.0.0.1", attempts=50)
    st.session_state.attacks.extend(new_attacks)
    alerts = detect_brute_force(st.session_state.attacks, threshold=5)
    st.session_state.alerts = alerts

if st.button("Run Simulation"):
    run_simulation()

st.subheader("Simulated Attacks (last 20 shown)")
for attack in st.session_state.attacks[-20:]:
    st.write(attack)

st.subheader("Alerts")
for alert in st.session_state.alerts:
    st.error(alert)

st.write("Auto-refreshing every 10 seconds...")

time.sleep(10)
st.experimental_rerun()
