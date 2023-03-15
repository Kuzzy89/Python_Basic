import math

record = float(input())
distance = float(input())
time = float(input())

sec_time = distance * time

slowing = math.floor(distance / 15) * 12.5

swimming_time = sec_time + slowing

diff = swimming_time - record
if record <= swimming_time:

    print(f"No, he failed! He was {diff:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {swimming_time:.2f} seconds.")




