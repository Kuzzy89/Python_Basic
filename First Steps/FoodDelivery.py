chicken = int(input())
fish = int(input())
vegi = int(input())

chicken_price = chicken * 10.35
fish_price = fish * 12.4
vegi_price = vegi * 8.15

all_menus = chicken_price + fish_price + vegi_price

dessert = all_menus * 0.2
delivery = 2.5
sum = all_menus + dessert + delivery

print(sum)

