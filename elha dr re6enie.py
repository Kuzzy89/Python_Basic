n = int(input())
for i in range(n + 1):
    stars = "*" * i
    space = " " * (n - i)
    print(space, end="")
    print(stars, end="")
    print(" | ", end="")
    print(stars, end="")
    print(space)

