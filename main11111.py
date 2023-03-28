age = int(input())
price = float(input())
toy_price = int(input())

brother_count = 0
total_sum = 0
money = 0
toys = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        toys += 1
    else:
        brother_count += 1
        money += 10
        total_sum += money

result = (toys * toy_price) + total_sum - brother_count

diff = abs(result - price)
if result >= price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")

