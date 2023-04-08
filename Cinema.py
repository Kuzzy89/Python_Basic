screen_type = input()
rows = int(input())
columns = int(input())

income = 0

hall = rows * columns

if screen_type == "Premiere":
    income = 12
elif screen_type == "Normal":
    income = 7.5
elif screen_type == "Discount":
    income = 5

all_income = income * hall

print(f"{all_income:.2f} leva")

