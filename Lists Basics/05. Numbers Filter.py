n = int(input())
even = []
odd = []
neg = []
pos = []

for i in range(n):
    number = int(input())

    if number % 2 == 0:
        even.append(number)
    if number % 2 != 0:
        odd.append(number)
    if number >= 0:
        pos.append(number)
    if number < 0:
        neg.append(number)

command = input()
if command == "even":
    print(even)
if command == "odd":
    print(odd)
if command == "negative":
    print(neg)
if command == "positive":
    print(pos)