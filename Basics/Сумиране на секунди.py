first_com = int(input())
second_com = int(input())
third_com = int(input())

sum = first_com + second_com + third_com
minutes = sum // 60
seconds = sum % 60

if seconds > 59:
    minutes += 1
    seconds = seconds - 60
if seconds > 59:
    minutes += 1
    seconds = seconds - 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")



