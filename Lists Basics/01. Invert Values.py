list_of_numbers = input().split()
opposite_nums = []
for element in list_of_numbers:
    current_num = -int(element)
    opposite_nums.append(current_num)

print(opposite_nums)