name = input()

grades_total = 0
all_num = 0
year_counter = 0
fails = 0

while True:
    number = float(input())
    year_counter += 1

    if number < 4:
        fails += 1
        if fails > 1:
            print(f" {name} has been excluded at {year_counter} grade")
            break

        year_counter -= 1

    else:
        grades_total += number

    if year_counter == 12:
        aver = grades_total / 12
        print(f"{name} graduated. Average grade: {aver:.2f}")
        break
