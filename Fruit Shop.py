fruit = input()
day = input()
quantity = float(input())
price = 0
flag = True

if day in ["Saturday", "Sunday"]:
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.9
    elif fruit == "grapefruit":
        price = 1.6
    elif fruit == "kiwi":
        price = 3.0
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
    else:
        flag = False
elif day in ["Tuesday", "Monday", "Wednesday", "Thursday", "Friday"]:
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85
    else:
        flag = False
else:
    flag = False

if flag:
    print("%.2f" % (quantity * price))
else:
    print("error")