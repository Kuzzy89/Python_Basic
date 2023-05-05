movie = input()
days = int(input())
tickets = int(input())
price_ticket = float(input())
percent = int(input()) / 100

sum_tickets_day = tickets * price_ticket
month_earn = days * sum_tickets_day
studio_price = month_earn * percent
all_price = month_earn - studio_price
print(f"The profit from the movie {movie} is {all_price:.2f} lv.")
