trip = float(input())

puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

toys_price = (puzzle * 2.6) + (doll * 3) + (bear * 4.1) + (minion * 8.2) + (truck * 2)

toys_count = puzzle + doll + bear + minion + truck

if toys_count >= 50:
    toys_price = toys_price - (toys_price * 0.25)
toys_price = toys_price - (toys_price * 0.1)
diff = abs(trip - toys_price)
if trip <= toys_price:
    print(f" Yes! {diff:.2f} lv left.")
else:
    print(f" Not enough money! {diff:.2f} lv needed.")





