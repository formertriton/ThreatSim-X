from collections import Counter

def detect_brute_force(attacks, threshold=10):
    ip_counter = Counter(a['source_ip'] for a in attacks if not a['success'])
    alerts = []
    for ip, count in ip_counter.items():
        if count > threshold:
            alerts.append({'source_ip': ip, 'failed_attempts': count, 'alert': 'Brute force detected'})
    return alerts
