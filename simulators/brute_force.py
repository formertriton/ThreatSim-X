import random
import time

def simulate_brute_force(target_ip, attempts=30):
    print(f"Simulating brute force attack on {target_ip} with {attempts} attempts...")
    attacks = []
    ip_pool = [f"192.168.1.{i}" for i in range(2, 10)]  # smaller pool of 8 IPs
    for i in range(attempts):
        source_ip = ip_pool[i % len(ip_pool)]  # cycle through same IPs
        timestamp = time.time()
        success = False
        attacks.append({'source_ip': source_ip, 'target_ip': target_ip, 'timestamp': timestamp, 'success': success})
        time.sleep(0.05)
    return attacks