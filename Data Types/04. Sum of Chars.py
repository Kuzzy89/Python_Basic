n = int(input())

all_score = 0

for _ in range(n):
    letter = input()
    all_score += ord(letter)

print(f"The sum equals: {all_score}")

