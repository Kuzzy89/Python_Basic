count_groups = int(input())

people_musala = 0
people_monblan = 0
people_kili = 0
people_k2 = 0
people_everest = 0

total_sum = 0
for i in range(1, count_groups + 1):
    count_people = int(input())
    total_sum += count_people

    if count_people <= 5:
        people_musala += count_people
    elif 6 <= count_people <= 12:
        people_monblan += count_people
    elif 13 <= count_people <= 25:
        people_kili += count_people
    elif 26 <= count_people <= 40:
        people_k2 += count_people
    elif count_people >= 41:
        people_everest += count_people

musala_percent = people_musala / total_sum * 100
print(f"{musala_percent:.2f}%")
monblan_percent = people_monblan / total_sum * 100
print(f"{monblan_percent:.2f}%")
kili_percent = people_kili / total_sum * 100
print(f"{kili_percent:.2f}%")
k2_percent = people_k2 / total_sum * 100
print(f"{k2_percent:.2f}%")
everest_percent = people_everest / total_sum * 100
print(f"{everest_percent:.2f}%")
