flag = False
total_money = 0

while True:
    destination = input()

    if destination == "End":
        flag = True
        break
    print()
    money_needed = float(input())

    while total_money < money_needed:
        money = float(input())
        total_money += money
    else:
        total_money = 0
        print(f"Going to {destination}!")