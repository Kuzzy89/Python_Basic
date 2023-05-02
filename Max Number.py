import sys
max = -sys.maxsize
number_init = 0

while True:
    number = input()
    if number == "Stop":
        break

    number_init = int(number)

    if number_init > max:
        max = number_init

print(max)