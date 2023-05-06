budget = float(input())

count = 0
budget_condition = False
needed_money = 0
cost = 0

while True:
    product = input()

    if product == "Stop":
        break

    price_of_product = float(input())

    count += 1

    if count % 3 == 0:
        price_of_product /= 2

    if price_of_product > budget:
        budget_condition = True
        needed_money = price_of_product - budget
        count -= 1
        break

    cost += price_of_product
    budget -= price_of_product


if not budget_condition:
    print(f"You bought {count} products for {cost:.2f} leva.")
else:
    print(f"You don't have enough money!")
    print(f"You need {needed_money:.2f} leva!")
