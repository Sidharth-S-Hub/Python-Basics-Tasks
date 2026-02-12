 ##   Create a function that:
	##	Takes a list of salaries
	##	Uses a loop to calculate total salary
	##	Returns the total


def calculate_total_salary(salaries):
    total = 0
    
    for salary in salaries:
        total += salary   # total = total + salary
    
    return total


# Example list
salary_list = [25000, 30000, 28000, 32000]

# Calling the function
total_salary = calculate_total_salary(salary_list)

print("Total Salary:", total_salary)
