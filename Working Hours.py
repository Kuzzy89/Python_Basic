hour = int(input())
day = input()

if 10 <= hour < 18:
    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
        print("open")
    else:
        print("closed")
else:
    print("closed")
