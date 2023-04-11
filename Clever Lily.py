age = int(input())
price = float(input())
toy_price = int(input())

money = 0
toys = 0
for i in range(1, age + 1):
    if age % 2 != 0:
        toys += 1
    else:
        money += 10

print()

