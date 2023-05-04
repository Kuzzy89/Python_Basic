failed_threshold = int(input())

solved_exam = 0 #решени упражнения
failed_times = 0 #грешки
sum_grades = 0  #сума от оценки
last_problem = ""
has_failed = True

input_line = input()

while input_line != "Enough":
    problem_name = input_line
    grade = int(input())

    if grade <= 4:
        failed_times += 1

    if failed_threshold <= failed_times:
        has_failed = False
        break

    sum_grades = sum_grades + grade
    solved_exam += 1
    last_problem = problem_name

    input_line = input()

if not has_failed:
    print(f"You need a break, {failed_times} poor grades.")
else:
    aver_score = sum_grades / solved_exam
    print(f"Average score: {aver_score:.2f}")
    print(f"Number of problems: {solved_exam}")
    print(f"Last problem: {last_problem}")