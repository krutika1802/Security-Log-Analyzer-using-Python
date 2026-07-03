from collections import Counter

with open("sample_logs.txt", "r") as file:
    logs = file.readlines()

failed_logins = []

for log in logs:
    if "Failed login attempt" in log:
        ip = log.split("IP")[-1].strip()
        failed_logins.append(ip)

counter = Counter(failed_logins)

print("\nSuspicious IP Addresses:\n")

for ip, count in counter.items():
    if count >= 2:
        print(f"IP Address: {ip} | Failed Attempts: {count}")