factor = int(input())
count = int(input())
list_of_nums = []

for i in range(1, count + 1):
    list_of_nums.append(i * factor)

print(list_of_nums)