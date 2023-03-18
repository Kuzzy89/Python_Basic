year = int(input())
def next_happy_year(year):
    year += 1
    while True:
        if len(set(str(year))) == 4:
            return year
        year += 1

print(next_happy_year(year))