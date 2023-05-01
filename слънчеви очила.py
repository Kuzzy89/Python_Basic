n = int(input())

print("*" * 2 * n, end="")
print(" " * n, end="")
print("*" * 2 * n)

for row in range(n - 2):
    if row == (n - 1) // 2 - 1:
        print("*" + "/" * (n * 2 - 2) + "*" + "|" * n + "*" + "/" * (n * 2 - 2) + "*")
    else:
        print("*" + "/" * (n * 2 - 2) + "*" + " " * n + "*" + "/" * (n * 2 - 2) + "*")

print("*" * 2 * n, end="")
print(" " * n, end="")
print("*" * 2 * n)