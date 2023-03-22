tax = int(input())

boots = tax - (tax * 0.4)
equip = boots - (boots * 0.2)
ball = equip * 1/4
accessories = ball * 1/5

sum = tax + boots + equip + ball + accessories

print(sum)