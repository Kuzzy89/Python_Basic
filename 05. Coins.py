change = float(input())
coins_change = change * 100

coins_count = 0
while True:
    if coins_change >= 200:
        coins_change -= 200
        coins_count += 1
    elif coins_change >= 100:
        coins_change -= 100
        coins_count += 1
    elif coins_change >= 50:
        coins_change -= 50
        coins_count += 1
    elif coins_change >= 20:
        coins_change -= 20
        coins_count += 1
    elif coins_change >= 10:
        coins_change -= 10
        coins_count += 1
    elif coins_change >= 5:
        coins_change -= 5
        coins_count += 1
    elif coins_change >= 2:
        coins_change -= 2
        coins_count += 1
    elif coins_change >= 1:
        coins_change -= 1
        coins_count += 1
    else:
        break
print(coins_count)