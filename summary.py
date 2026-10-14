import sys
from collections import Counter

filename = sys.argv[1]
pos = int(sys.argv[2]) if len(sys.argv) > 2 else 7

with open(filename) as f:
    lines = f.readlines()

print("Total lines:", len(lines))
print()

counts = Counter()
for line in lines:
    fields = line.split()
    if len(fields) > pos:
        key = fields[pos]
        counts[key] += 1

print("Top 5:\n")
for item, n in counts.most_common(5):
    print(item, n)
