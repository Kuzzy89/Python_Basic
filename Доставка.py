chiken_menu_count = int(input())
fish_menu_count = int(input())
vegi_menu_count = int(input())

price_chiken = chiken_menu_count * 10.35
price_fish = fish_menu_count * 12.4
price_vegi = vegi_menu_count * 8.15

all_price_menu = price_chiken + price_fish + price_vegi
dessert_price = all_price_menu * 0.2

total_sum = all_price_menu + dessert_price + 2.5

print(total_sum)
