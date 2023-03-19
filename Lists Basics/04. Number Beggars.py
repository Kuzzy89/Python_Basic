money_list = input().split(", ")
number_of_beggars = int(input())
finale_sums = []
money_list_as_digits = []
starting_index = 0
for element in money_list:
    money_list_as_digits.append(int(element))
while starting_index < number_of_beggars:
    sum_of_current_beggar = 0
    for current_index in range(starting_index, len(money_list_as_digits), number_of_beggars):
        sum_of_current_beggar += money_list_as_digits[current_index]
    finale_sums.append(sum_of_current_beggar)
    starting_index += 1

print(finale_sums)