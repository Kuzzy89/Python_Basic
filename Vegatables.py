vegetables_price = float(input())
fruit_price = float(input())
vegetables_kg = int(input())
fruits_kg = int(input())

vegetables_total_price = vegetables_price * vegetables_kg
fruits_total_price = fruit_price * fruits_kg


print((vegetables_total_price + fruits_total_price) / 1.94)
