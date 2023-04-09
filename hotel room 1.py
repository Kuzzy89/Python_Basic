month = input()
days = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = days * 50
    apartment = days * 65
elif month == "June" or month == "September":
    studio = days * 75.2
    apartment = days * 68.7
elif month == "July" or month == "August":
    studio = days * 76
    apartment = days * 77
if days > 14 and month == "May" or month == "October":
    studio *= 0.7
elif days > 7 and month == "May" or month == "October":
    studio *= 0.95
elif days > 14 and month == "June" or month == "September":
    studio *= 0.8
if days > 14:
    apartment *= 0.9
print(f"Apartment: {apartment:.2f} lv.")
print(f"Studio: {studio:.2f} lv.")


