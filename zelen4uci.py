vegetables_price = float(input())
fruits_price = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

veg = vegetables_price * vegetables_kg
fru = fruits_price * fruits_kg

print((veg + fru) / 1.94)
