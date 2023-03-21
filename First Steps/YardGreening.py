square_meter = float(input()) * 7.61
disscount = square_meter * 0.18

price = square_meter - disscount
print(f"The final price is {price} lv.")
print(f"The discount is {disscount} lv.")