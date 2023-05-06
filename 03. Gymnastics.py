country = input()
device = input()

dific = 0
perform = 0

if country == "Russia":
    if device == "ribbon":
        dific = 9.100
        perform = 9.400
    elif device == "hoop":
        dific = 9.300
        perform = 9.800
    elif device == "rope":
        dific = 9.600
        perform = 9.000
elif country == "Bulgaria":
    if device == "ribbon":
        dific = 9.600
        perform = 9.400
    elif device == "hoop":
        dific = 9.550
        perform = 9.750
    elif device == "rope":
        dific = 9.500
        perform = 9.400
elif country == "Italy":
    if device == "ribbon":
        dific = 9.200
        perform = 9.500
    elif device == "hoop":
        dific = 9.450
        perform = 9.350
    elif device == "rope":
        dific = 9.700
        perform = 9.150

all_sum = dific + perform
percent = ((20 - all_sum) / 20) * 100
print(f"The team of {country} get {all_sum:.3f} on {device}.")
print(f"{percent:.2f}%")
