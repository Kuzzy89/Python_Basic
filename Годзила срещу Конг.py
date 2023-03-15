budget = float(input())
statists = int(input())
clothes = float(input())

decor = budget * 0.1
sum_clothes = statists * clothes

if statists > 150:
    sum_clothes = sum_clothes - (sum_clothes * 0.1)

movie_price = decor + sum_clothes

diff = abs(budget - movie_price)
if budget >= movie_price:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")