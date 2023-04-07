a = int(input())
b = int(input())
m = int(input())

flag = False

count = 0


for x in range(a, b + 1):
    for y in range(a, b + 1):
        count += 1
        if x + y == m:
            print(f"Combination N:{count} ({x} + {y} = {m})")
            flag = True
            break

    if flag:
        break

if not flag:
    print(f"{count} combinations - neither equals {m}")





