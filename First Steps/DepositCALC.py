deposit = float(input())
months = int(input())
GPI = float(input())

sum = deposit + months * ((deposit * GPI/100) / 12)
print(sum)