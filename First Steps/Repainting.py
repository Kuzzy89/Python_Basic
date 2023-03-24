nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = (nylon + 2) * 1.5
paint_price = (paint + ( paint * 0.1)) * 14.5
thinner_price = thinner * 5
bags = 0.4

price_matterials = nylon_price + paint_price + thinner_price + bags
work_price = (price_matterials * 0.3) * hours
all_prise = price_matterials + work_price

print(all_prise)