budget = float(input())
number_of_nights = int(input())
price_night = float(input())
percent = int(input()) / 100

if number_of_nights > 7:
    price_night -= price_night * 0.05

costs = number_of_nights * price_night
additional_cost = budget * percent
all_cost = costs + additional_cost

diff = abs(budget - all_cost)

if budget >= all_cost:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")