from datetime import datetime, timedelta

date_string = input()
date_object = datetime.strptime(date_string, "%Y-%m-%d").date()
new_date = date_object + timedelta(days=1000)
new_date_string = new_date.strftime("%d-%m-%Y")
print(new_date_string)