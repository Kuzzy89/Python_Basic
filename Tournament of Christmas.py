days = int(input())
sbor_money = 0
all_wins = 0
all_lose = 0

for i in range(1, days + 1):
    wins = 0
    lose = 0
    money_earned = 0
    command = input()
    while command != "Finish":
        result = input()

        if result == "win":
            money_earned += 20
            wins += 1
            all_wins += 1
        elif result == "lose":
            lose += 1
            all_lose += 1

        command = input()

    if wins > lose:
        money_earned += money_earned * 0.1
        sbor_money += money_earned
    else:
        sbor_money += money_earned

if all_wins > all_lose:
    sbor_money += sbor_money * 0.2
    print(f"You won the tournament! Total raised money: {sbor_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {sbor_money:.2f}")