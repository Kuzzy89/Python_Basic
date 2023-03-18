centuries = int(input())

y = centuries * 100
d = int(y * 365.2422)
h = int(d * 24)
m = int(h * 60)

print(f"{centuries} centuries = {y} years = {d} days = {h} hours = {m} minutes")