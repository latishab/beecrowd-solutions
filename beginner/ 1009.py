# input values
name = input()
fixed_salary = input()
sales = input()

# count final salary
final_salary = float(fixed_salary) + (float(sales)*0.15)
final_salaryf = "{:.2f}".format(final_salary)

print("TOTAL = R$", final_salaryf)
