initial_energy = 100
initial_coins = 100

events = input().split("|")
factory_is_open = True

for event in events:
    event_info = event.split("-")

    event_type = event_info[0]
    event_number = int(event_info[1])

    if event_type == "rest":
        current_energy = initial_energy
        initial_energy += event_number

        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")

    elif event_type == "order":
        if initial_energy - 30 >= 0:
            initial_coins += event_number
            initial_energy -= 30
            print(f"You earned {event_number} coins.")
        else:
            initial_energy += 50
            print(f"You had to rest!")

    else:
        if initial_coins >= event_number:
            initial_coins -= event_number
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            factory_is_open = False
            break

if factory_is_open:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")
