number_of_lines = int(input())
even_sum = 0
odd_sum = 0
for i in range(1, number_of_lines + 1):
    current_num = int(input())
    if i % 2 == 0:
        even_sum += current_num
    else:
        odd_sum += current_num

diff = abs(odd_sum - even_sum)
if diff == 0:
    print(f"Yes")
    print(f"Sum = {odd_sum}")
else:
    print(f"No")
    print(f"Diff = {diff}")
