import sys

n = int(input())
max_number = -sys.maxsize
sum_numbers = 0

for i in range(1, n + 1):
    number = int(input())

    sum_numbers += number

    if number > max_number:
        max_number = number

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum ={sum_numbers}")
else:
    print("No")
    sum_numbers = sum_numbers - max_number
    print(f"Diff = {abs(max_number - sum_numbers)}")