n = int(input())

space = 0
star = "*"
second_star = n-1

for row in range(1, 2*n):
    if row <= n:
        space = n - row
        star = row
        print(" " * space + "* " * star)
    else:
        space = row - n
        print(" " * space + "* " * second_star)
        second_star -=1