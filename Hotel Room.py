month = input()
days = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < days <= 13:
        studio = studio - (studio * 0.05)
        studio_price = studio * days
        apartment_price = apartment * days
        print(f" Apartment: {apartment_price:.2f}lv.")
        print(f" Studio: {studio_price:.2f} lv.")

    elif days > 14:
        apartment = apartment - (apartment * 0.1)
        apartment_price = apartment * days

        studio = studio - (studio * 0.3)
        studio_price = studio * days
        print(f" Apartment: {apartment_price:.2f} lv.")
        print(f" Studio: {studio_price:.2f} lv.")
    else:
        studio_price = studio * days
        apartment_price = apartment * days
        print(f" Apartment: {apartment_price:.2f} lv.")
        print(f" Studio: {studio_price:.2f} lv.")


elif month == "June" or month == "September ":
    studio = 75.2
    apartment = 68.7
    if days > 14:
        apartment = apartment - (apartment * 0.1)
        apartment_price = apartment * days

        studio_price = studio * days

        print(f" Apartment: {apartment_price:.2f} lv.")
        print(f" Studio: {studio_price:.2f} lv.")
    else:
        apartment_price = apartment * days

        studio_price = studio * days

        print(f" Apartment: {apartment_price:.2f} lv.")
        print(f" Studio: {studio_price:.2f} lv.")

elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if days > 14:
        apartment = apartment - (apartment * 0.1)
        apartment_price = apartment * days

        studio_price = studio * days

        print(f" Apartment: {apartment_price:.2f} lv.")
        print(f" Studio: {studio_price:.2f} lv.")
    else:
        apartment_price = apartment * days

        studio_price = studio * days

        print(f" Apartment: {apartment_price:.2f} lv.")
        print(f" Studio: {studio_price:.2f} lv.")
