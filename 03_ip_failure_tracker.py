# 03_ip_failure_tracker.py
# Advanced SOC audit: Tracking and grouping failed attempts by IP address

logs = [
    "2026-10-29 10:02:14 - FAILED login attempt from IP 192.168.1.45",
    "2026-10-29 10:02:18 - FAILED login attempt from IP 192.168.1.45",
    "2026-10-29 10:03:01 - FAILED login attempt from IP 10.0.0.12",
    "2026-10-29 10:03:15 - FAILED login attempt from IP 192.168.1.45",
    "2026-10-29 10:04:00 - User 'sarah' logged in successfully."
]

# Dictionary to store { "IP_ADDRESS": count }
failed_ip_counts = {}

for log in logs:
    if "FAILED" in log:
        # Extract the IP address after the string "IP "
        ip = log.split("IP ")[1]
        
        # Increment failure count for this specific IP
        if ip in failed_ip_counts:
            failed_ip_counts[ip] += 1
        else:
            failed_ip_counts[ip] = 1

print("=== SOC Per-IP Threat Analysis ===")

for ip, count in failed_ip_counts.items():
    print(f"IP Target: {ip} | Total Failures: {count}")
    if count >= 3:
        print(f"  [ACTION] Automatically pushing {ip} to Firewall Blocklist!")