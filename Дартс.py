player_name = input()
successful_shots_counter = 0
unsuccessful_shots_counter = 0
points = 301

while points > 0:
    command = input()

    if command == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots_counter} unsuccessful shots.")
        break

    current_points = int(input())

    if command == "Single":
        pass
    elif command == "Double":
        current_points *= 2
    elif command == "Triple":
        current_points *= 3

    if current_points > points:
        unsuccessful_shots_counter += 1
        continue

    points -= current_points
    successful_shots_counter += 1

if points == 0:
    print(f"{player_name} won the leg with {successful_shots_counter} shots.")