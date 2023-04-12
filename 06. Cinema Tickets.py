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

    while ticket_type != "End":
        tick_type = ticket_type
        if tick_type == "student":
            count_student_ticket += 1
            all_tickets += 1
            all_students_tickets += 1
            total_tickets += 1
        elif tick_type == "standard":
            count_standard_ticket += 1
            all_tickets += 1
            all_standard_tickets += 1
            total_tickets += 1
        elif tick_type == "kid":
            count_kid_ticket += 1
            all_tickets += 1
            all_kid_tickets += 1
            total_tickets += 1
        if seats == total_tickets:
            break
        ticket_type = input()
    percent_total_tickets = total_tickets / seats * 100
    print(f"{movie} - {percent_total_tickets:.2f}% full.")
    input_line = input()
print(f"Total tickets: {all_tickets}")
per_standard_tickets = all_standard_tickets / all_tickets * 100
per_students_tickets = all_students_tickets / all_tickets * 100
per_kid_tickets = all_kid_tickets / all_tickets * 100
print(f"{per_students_tickets:.2f}% student tickets.")
print(f"{per_standard_tickets:.2f}% standard tickets.")
print(f"{per_kid_tickets:.2f}% kids tickets.")
