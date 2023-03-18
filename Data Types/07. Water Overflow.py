n = int(input())
capacity = 255
all_liters = 0
for i in range(n):
    liters = int(input())

    if all_liters + liters > capacity:
        print(f"Insufficient capacity!")
    else:
        all_liters += liters

print(all_liters)
