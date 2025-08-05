import random
import time

def simulate_brute_force(target_ip, attempts=30):
    print(f"Simulating brute force attack on {target_ip} with {attempts} attempts...")
    attacks = []
    for i in range(attempts):
        source_ip = f"192.168.1.{random.randint(2,254)}"
        timestamp = time.time()
        success = False
        attacks.append({'source_ip': source_ip, 'target_ip': target_ip, 'timestamp': timestamp, 'success': success})
        time.sleep(0.05)
    return attacks
