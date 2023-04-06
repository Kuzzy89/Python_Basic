flag = False
total_budget = 0

while True:
    destination = input()
    if destination == "End":
        flag = True
        break

    needed_budget = float(input())

    while total_budget > needed_budget:
        current_budget = float(input())
        total_budget += current_budget
    else:
        total_budget = 0
        print(f"Going to {destination}!")




