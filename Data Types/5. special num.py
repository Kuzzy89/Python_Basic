n = int(input())

for i in range(1, n + 1):
    is_special = False
    i_as_str = str(i)
    sum_of_digits = 0

    for char in i_as_str:
        sum_of_digits += int(char)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        is_special = True

    print(f"{i} -> {is_special}")