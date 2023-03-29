name = input()
point_from_academy = float(input())
count_judge = int(input())

stack_points = point_from_academy

for i in range(1, count_judge + 1):
    judge = input()
    points = float(input())

    current_point = (len(judge) * points) / 2
    stack_points = stack_points + current_point

    if stack_points >= 1250.5:
        break

if stack_points >= 1250.5:
    print(f"Congratulations, {name} got a nominee for leading role with {stack_points:.1f}!")
else:
    diff = 1250.5 - stack_points
    print(f"Sorry, {name} you need {diff:.1f} more!")
