needed_money = float(input())
current_money = float(input())

total_sum = current_money
days = 0
spend_days = 0

while True:
    command = input()
    money = float(input())
    if command == "spend":
        spend_days += 1
        days += 1
        total_sum -= money
        if total_sum < 0:
            total_sum = 0

        if spend_days == 5:
            print(f"You can't save the money.")
            print(days)
            break

    elif command == "save":
        total_sum += money
        days += 1

    if total_sum >= needed_money:
        print(f"You saved the money for {days} days.")
        break