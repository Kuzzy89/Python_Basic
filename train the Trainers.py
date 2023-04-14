juri = int(input())

input_line = input()
big_counter = 0
big_grade_counter = 0

while input_line != "Finish":
    presentation = input_line
    counter = 0
    all_grades = 0

    for i in range(1, juri + 1):
        current_grade = float(input())
        counter += 1
        all_grades += current_grade
        big_counter += 1
        big_grade_counter += current_grade

    average_grades = all_grades / counter
    input_line = input()
    print(f"{presentation} - {average_grades:.2f}.")

last = big_grade_counter / big_counter

print(f"Student's final assessment is {last:.2f}.")
