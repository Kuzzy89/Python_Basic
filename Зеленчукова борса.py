price_vegatables_kg = float(input())
price_friuts_kg = float(input())
vegatables_kg = int(input())
fruits_kg = int(input())

vegatables = price_vegatables_kg*vegatables_kg
fruits = price_friuts_kg*fruits_kg
sum = vegatables+ fruits
sum_to_euro = sum/1.94
print(sum_to_euro)