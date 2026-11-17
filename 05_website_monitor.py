# 05_website_monitor.py
# Automated website availability and response-time monitor

import time
from datetime import datetime
import requests

websites = [
    "https://github.com",
    "https://www.ncsc.gov.uk",
    "https://www.bbc.co.uk",
    "https://outlook.live.com",
    "https://www.youtube.com"
]
CHECK_INTERVAL = 60 * 60  # 3,600 seconds (1 hour)

print("Starting Live Website Monitor... (Press Ctrl+C in terminal to stop)")

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n=== Network Status Report [{timestamp}] ===")

    for url in websites:
        try:
            response = requests.head(url, timeout=5, allow_redirects=True)
            
            # Fall back to a lightweight GET if the server blocks HEAD (405)
            if response.status_code == 405:
                with requests.get(url, timeout=5, allow_redirects=True, stream=True) as get_resp:
                    status = get_resp.status_code
                    speed_ms = round(get_resp.elapsed.total_seconds() * 1000)
            else:
                status = response.status_code
                speed_ms = round(response.elapsed.total_seconds() * 1000)

            if status == 200:
                print(f"[ONLINE]  {url} | Code: {status} | Speed: {speed_ms}ms")
            else:
                print(f"[WARNING] {url} | Code: {status} | Speed: {speed_ms}ms")

        except requests.exceptions.RequestException:
            print(f"[OFFLINE] {url} | Connection failed or timed out")

    print("Report complete. Sleeping for 1 hour...")
    time.sleep(CHECK_INTERVAL)