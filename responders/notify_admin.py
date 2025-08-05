def notify_admin(alert):
    print(f"[ALERT] Admin notified: {alert['alert']} from IP {alert['source_ip']} with {alert['failed_attempts']} failed attempts.")
