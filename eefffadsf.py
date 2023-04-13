all_tickets = 0
all_students_tickets = 0
all_standard_tickets = 0
all_kid_tickets = 0

input_line = input()

while input_line != "Finish":
    movie = input_line
    seats = int(input())
    count_student_ticket = 0
    count_standard_ticket = 0
    count_kid_ticket = 0
    total_tickets = 0

    ticket_type = input()

    percent_total_tickets = total_tickets / seats * 100
    print(f"{movie} - {percent_total_tickets:.2f}% full.")
    input_line = input()
print(f"Total tickets: {all_tickets}")