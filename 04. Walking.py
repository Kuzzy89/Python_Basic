input_line = input()

all_pace = 0

while input_line != "Going home":
    pace = int(input_line)
    all_pace += pace
    if all_pace >= 10000:
        break

    input_line = input()

if input_line == "Going home":
    home_steps = int(input())
    all_pace += home_steps

diff = abs(all_pace - 10000)
if all_pace >= 10000:
    print(f"Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")