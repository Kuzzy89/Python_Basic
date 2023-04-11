degree = int(input())
day = input()
Outfit = ""
Shoes = ""

if day == "Morning":
    if 10 <= degree <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif 18 < degree <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    else:
        degree >= 25
        Outfit = "T-Shirt"
        Shoes = "Sandals"
elif day == "Afternoon":
    if 18 < degree <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    elif 18 < degree <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    else:
        degree >= 25
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
elif day == "Evening":
    if 18 < degree <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif 18 < degree <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    else:
        degree >= 25
        Outfit = "Shirt"
        Shoes = "Moccasins"
print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
