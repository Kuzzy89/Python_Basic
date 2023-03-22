length = int(input())
width = int(input())
height = int(input())
percentage = float(input()) / 100

area = length * width * height
area_litters = area/1000
taken_place = percentage

litters_needed = area_litters * (area_litters - taken_place)

print(litters_needed)

