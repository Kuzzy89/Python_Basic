import math
count_tours = int(input())
start_points = int(input())

points = start_points
win = 0
for i in range(1, count_tours + 1):
    phase = input()

    if phase == "W":
        win += 1
        points += 2000
    elif phase == "F":
        points += 1200
    elif phase == "SF":
        points += 720

average_points = math.floor((points - start_points) / count_tours)
win_percent = win/count_tours * 100

print(f"Final points: {points}")
print(f"Average points: {average_points}")
print(f"{win_percent:.2f}%")


