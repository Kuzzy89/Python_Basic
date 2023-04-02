import math

figure = input()
area = 0.0
a = float(input())
if figure == "square":
    area = a * a
elif figure == "rectangle":
    b = float(input())
    area = a * b
elif figure == "circle":
    area = math.pi * math.pow(a, 2)
elif figure == "triangle":
    h = float(input())
    area = (a * h) / 2
print("%.3f" % area)  #(f"{area:.3f}")




