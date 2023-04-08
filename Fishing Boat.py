budget = int(input())
season = input()
count_fishmen = int(input())

price = 0

if season == "Spring":
    price = 3000
    if count_fishmen <= 6:
        price = price * 0.9
    elif 7 < count_fishmen <= 11:
        price = price * 0.85
    elif count_fishmen > 12:
        price = price * 0.75
elif season == "Summer":
    price = 4200
    if count_fishmen <= 6:
        price = price * 0.9
    elif 6 < count_fishmen <= 11:
        price = price * 0.85
    elif count_fishmen > 12:
        price = price * 0.75
elif season == "Autumn":
    price = 4200
    if count_fishmen <= 6:
        price = price * 0.9
    elif 6 < count_fishmen <= 11:
        price = price * 0.85
    elif count_fishmen > 12:
        price = price * 0.75
elif season == "Winter":
    price = 2600
    if count_fishmen <= 6:
        price = price * 0.9
    elif 6 < count_fishmen <= 11:
        price = price * 0.85
    elif count_fishmen > 12:
        price = price * 0.75

if season != "Autumn" and count_fishmen % 2 == 0:
    price = price * 0.95

diff = abs(budget - price)

if budget > price:
    print(f"Yes! You have {diff:.2f} leva left.")
elif budget < price:
    print(f"Not enough money! You need {diff:.2f} leva.")


