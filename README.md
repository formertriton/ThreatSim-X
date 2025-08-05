# ThreatSim-X -- Threat Simulation & Response Framework
Goal: Build a modular framework to simulate basic cyber/physical threats and test response workflows perfect for DevSecOps, space systems, or smart infrastructure themes.

# 🚀 Overview

ThreatSim-X is a modular, Python-based framework for simulating and detecting cyber threats, triggering automated responses, and logging incidents. Ideal for cybersecurity demos in DevSecOps, smart infrastructure, or space systems contexts.

# 🎯 Objectives

Simulate typical cyber attacks (e.g., brute-force, port scanning, malware detection)

Build a modular monitoring and detection pipeline

Automate response actions (IP blocking, alerting, logging)

Log incidents and generate reports for analysis

Provide a sandbox for experimenting with threat models and response strategies

# 🔥 Key Features

Realistic Threat Simulations: Brute force, port scanning, malware indicators

Pluggable Detection Engines: Threshold-based and signature/rule-based logic

Automated Mock Responses: Logging, IP blocking, alerting (print/email/etc.)

Human-Readable Logging: Structured logs in JSON or text format

Easy Configuration: Modify detection thresholds and rules via YAML

# 📦 Project Structure
```
threatsim-x/
├── main.py                  # Entry point for simulation orchestration
├── config/                 
│   └── thresholds.yaml      # Detection configuration
├── simulators/             
│   ├── brute_force.py       # Simulates login brute-force attacks
│   ├── port_scan.py         # Simulates port scanning
│   ├── malware_dropper.py   # Simulates malware activity
├── detectors/              
│   ├── anomaly_detector.py  # Behavioral/anomaly-based detection
│   └── signature_engine.py  # Rule/signature-based detection
├── responders/
│   ├── block_ip.py          # IP blocking logic (mock)
│   ├── logger.py            # Logs incidents to file
│   └── notify_admin.py      # Simulates alert notification
├── data/
│   └── logs/                # Incident reports and logs
├── utils/
│   └── helpers.py           # Shared utility functions
├── tests/
│   └── test_simulations.py  # Unit tests for simulators and logic
├── requirements.txt
└── README.md
```
<img width="489" height="545" alt="Screenshot 2025-08-04 182732" src="https://github.com/user-attachments/assets/6433146c-bd6a-4ca4-a5d9-f080bc674586" />

<img width="489" height="545" alt="Screenshot 2025-08-04 182732" src="https://github.com/user-attachments/assets/3ec63bb0-8a9b-4085-8ac8-34f62386f186" />
<img width="719" height="332" alt="Screenshot 2025-08-04 182744" src="https://github.com/user-attachments/assets/f5580714-606b-4120-a302-45405daa45b2" />

# ✅ Getting Started

1. Clone the repository:
```
git clone https://github.com/formertriton/ThreatSim-X.git
cd ThreatSim-X
```
2. Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
3. Run the simulation:
```
python main.py
```
4. (Optional) Launch the dashboard:
```
streamlit run app.py
```
# 🛠 Technologies & Tools

Python 3.11+

socket, subprocess — for simulating activity

logging, json — for incident capture and logging

PyYAML — for configuration

pytest — for unit testing

(Optional) streamlit or flask — for UI/dashboard

# 📄 License

MIT License — see LICENSE file for details.
