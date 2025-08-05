blocked_ips = set()

def block_ip(ip):
    blocked_ips.add(ip)
    print(f"[RESPONDER] Blocking IP: {ip}")
