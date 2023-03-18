budget = float(input())
video_card_num = int(input())
processor_num = int(input())
ram_num = int(input())

video_card_price = video_card_num * 250
processor_price = (video_card_price * 0.35) * processor_num
ram_price = (video_card_price * 0.1) * ram_num

disscount = 0

price = video_card_price + processor_price + ram_price + disscount

if video_card_num > processor_num:
    disscount = price * 0.15

price_with_discount = price - disscount

diff = abs(budget - price_with_discount)

if price_with_discount < budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")



