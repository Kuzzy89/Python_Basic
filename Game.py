games_sold = int(input())

Hearthstone = 0
Fornite = 0
Overwatch = 0
Others = 0

for i in range(games_sold):
    game = input()
    if game == "Hearthstone":
        Hearthstone += 1
    elif game == "Fornite":
        Fornite += 1
    elif game == "Overwatch":
        Overwatch += 1
    else:
        Others += 1

hearthstone_percent = (Hearthstone * 100) / games_sold
fornite_percent = (Fornite * 100) / games_sold
overwatch_percent = (Overwatch * 100) / games_sold
other_percent = (Others * 100) / games_sold
print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print(f"Others - {other_percent:.2f}%")