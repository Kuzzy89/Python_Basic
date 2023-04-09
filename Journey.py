budget = float(input())
season = input()

destination = ""
place = ""
expenses = 0

if budget < 100:
    destination = "Bulgaria"
    if season == "Summer":
        place = "Camp"
        expenses = budget * 0.3
    else:
        place = "Hotel"
        expenses = budget * 0.7
elif budget < 1000:
    destination = "Balkans"
    if season == "Summer":
        place = "Camp"
        expenses = budget * 0.4
    else:
        place = "Hotel"
        expenses = budget * 0.8
elif budget > 1000:
    destination = "Europe"
    place = "Hotel"
    expenses = budget * 0.90

print(f"Somewhere in {destination}")
print(f"{place} - {expenses:.2f}")