book_sheets = int(input())
red_sheet_per_hour = int(input())
days = int(input())

hours = ((book_sheets/red_sheet_per_hour) // days)
print(hours)

