n = int(input())
pos = []
neg = []

for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        pos.append(current_number)
    else:
        neg.append(current_number)

print(pos)
print(neg)
print(f"Count of positives: {len(pos)}")
print(f"Sum of negatives: {sum(neg)}")
