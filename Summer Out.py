flowers = input()
count_flowers = int(input())
budget = int(input())

#roses_price = 5
#dahlias_price = 3.8
#tulips = 2.8
#narcissus = 3
#gladiolus = 2.5

price = 0

if flowers == "Roses":
    price = 5
elif flowers == "Dahlias":
    price = 3.8
elif flowers == "Tulips":
    price = 2.8
elif flowers == "Narcissus":
    price = 3
elif flowers == "Gladiolus":
    price = 2.5

total_price = count_flowers * price
if flowers == "Roses" and count_flowers > 80:
    total_price = total_price * 0.9
elif flowers == "Dahlias" and count_flowers > 90:
    total_price = total_price * 0.85
elif flowers == "Tulips" and count_flowers > 90:
    total_price = total_price * 0.85
elif flowers == "Narcissus" and count_flowers < 120:
    total_price = total_price * 1.15
elif flowers == "Gladiolus" and count_flowers < 80:
    total_price = total_price * 1.20


diff = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {count_flowers} {flowers} and {diff:.2f} leva left.")
elif budget < total_price:
    print(f"Not enough money, you need {diff:.2f} leva more.")









