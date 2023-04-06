import sys
n = int(input())

max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
print({max_number})
print({min_number})



