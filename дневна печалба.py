working_days = int(input())
salary_per_day = float(input())
one_dollar = float(input())

one_month_salary = working_days * salary_per_day
year_salary = one_month_salary * 12
bonus = one_month_salary * 2.5
tax = (year_salary + bonus) * 0.25

salary_after_tax = (year_salary + bonus) - tax

lev_per_day = (salary_after_tax/ 365) * one_dollar

print(round(lev_per_day, 2))



