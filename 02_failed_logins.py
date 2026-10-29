
    # 02_failed_logins.py
# Simple log auditor to detect repeated authentication failures

logs = [
    "2026-10-29 10:00:01 - User 'admin' logged in successfully.",
    "2026-10-29 10:02:14 - FAILED login attempt from IP 192.168.1.45",
    "2026-10-29 10:02:18 - FAILED login attempt from IP 192.168.1.45",
    "2026-10-29 10:02:22 - FAILED login attempt from IP 192.168.1.45",
    "2026-10-29 10:05:00 - User 'sarah' logged in successfully."
]

failed_count = 0

print("=== SOC Authentication Log Audit ===")

for log in logs:
    if "FAILED" in log:
        failed_count += 1
        print(f"[FLAGGED] {log}")

print("------------------------------------")
print(f"Total Failed Attempts Detected: {failed_count}")

if failed_count >= 3:
    print("ACTION REQUIRED: Potential brute-force attack detected!")