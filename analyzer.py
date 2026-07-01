import re
from collections import Counter
log_file = "auth.log"
failed_pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"
failed_ips = []

with open(log_file, "r") as file:
    for line in file:
        match = re.search(failed_pattern, line)
        if match:
            failed_ips.append(match.group(1))
counter = Counter(failed_ips)
print("=" * 40)
print("failed log analysis")
print("=" * 40)
for ip, count in counter.items():
    print(f"{ip} -> {count} failed attempts")


