import math

i = float(input()) * 100
w = float(input()) * 100
w -= 100

rows = i//120
buros_in_row = w//70

all_buros = (rows * buros_in_row) -3
print(math.trunc(all_buros))