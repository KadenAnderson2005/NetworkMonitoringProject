import subprocess
import re

print("Network Monitor Starting...")

def check_connection(ip_address):
    result = subprocess.run(
        ["ping", "-n", "1", "-w", "1000", ip_address],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        match = re.search(
            r"time[=<]\s*(\d+)\s*ms",
            result.stdout,
            re.IGNORECASE
)

        if match:
            response_time = int(match.group(1))
        else:
            response_time = 0

        return {
            "ip": ip_address,
            "status": "Online",
            "response_time": response_time
        }

    return{
        "ip": ip_address,
        "status": "Offline",
        "response_time": None
    }

def monitor_network():
    devices = [
        "1.1.1.1",
        "8.8.8.8",
        "google.com"
    ]

    for device in devices:
        result = check_connection(device)

        print("----------------------")
        print("IP/Host:", result["ip"])
        print("Status:", result["status"])
        print("Response Time:", result["response_time"], "ms")

if __name__ == "__main__":
    monitor_network()