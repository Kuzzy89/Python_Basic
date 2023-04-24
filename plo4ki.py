n = int(input())
w = float(input())
l = float(input())
m = int(input())
o = int(input())

area_square = n * n
area_bench = m * o
area_work = area_square - area_bench

area_tile = w * l

number_tile = area_work / area_tile
time = number_tile * 0.2

print("Плочки " + str(round(number_tile, 2)))
print("Време " + str(round(time, 2)))
