total_sum = 0


while True:
    increase = input()
    if increase == "NoMoreMoney":
        break

    increase = float(increase)

    if float(increase) >= 0:
        total_sum += float(increase)
        print(f"Increase: {float(increase):.2f}")
    elif float(increase) < 0:
        print("Invalid operation!")
        print(f"Total: {total_sum:.2f}")
        break
    elif increase == "NoMoreMoney":
        print(f"Total: {total_sum:.2f}")