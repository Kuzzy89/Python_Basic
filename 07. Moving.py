width = int(input())
length = int(input())
height = int(input())

area = width * length * height
sum_boxes = 0
input_line = input()
while input_line != "Done":
    boxes = int(input_line)
    sum_boxes += boxes

    if sum_boxes >= area:
        break

    input_line = input()
diff = abs(sum_boxes - area)

if sum_boxes > area:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")