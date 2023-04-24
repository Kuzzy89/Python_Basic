x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

widht = max(x1, x2) - min(x1, x2)
height = max(y1, y2) - min(y1, y2)

area = widht * height
parimeter = 2 * (widht + height)
print("Area = ", area)
print("Parameter = ", parimeter)
