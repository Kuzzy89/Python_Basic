from math import ceil

height = int(input())
weight = int(input())
no_painting = int(input())

command = input()

perimeter = height * weight * 4
walls_for_painting = ceil(perimeter - (no_painting * 0.01 * perimeter))


while command != "Tired!":
    litters_paint = int(command)
    walls_for_painting -= litters_paint
    if walls_for_painting < 0:
        print(f"All walls are painted and you have {abs(walls_for_painting)} l paint left!")
        break
    if walls_for_painting == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break
    command = input()
if command == "Tired!":
    print(f"{abs(walls_for_painting)} quadratic m left.")

