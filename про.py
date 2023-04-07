total_sum = 0
helper = 0

while True:
    increase = input()
        if increase != "NoMoreMoney":
            helper = increase
            if float(helper) >= 0:
            total_sum += float(helper)
            print(f"Increase: {float(helper):.2f}")
                elif float(helper) < 0:
                print("Invalid operation!")
                print(f"Total: {total_sum:.2f}")
                    break
                 elif increase == "NoMoreMoney":
                    print(f"Total: {total_sum:.2f}")