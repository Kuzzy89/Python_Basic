n = int(input())

stars = 2 * n
space = n
slash = 2 * n - 2

print("*" * stars + " " * space + "*" * stars)

for row in range(n - 2):
    if row == (n - 1) // 2 - 1:
        print("*" + "/" * slash + "*" + "|" * space + "*" + "/" * slash + "*")
    else:
        print("*" + "/" * slash + "*" + " " * space + "*" + "/" * slash + "*")
print("*" * stars + " " * space + "*" * stars)
