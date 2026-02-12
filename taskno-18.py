 ##   Create a function that asks the user for their birth year and returns their age. (No arguments, but has a return)


def calculate_age():
    birth_year = int(input("Enter your birth year: "))
    current_year = 2026
    age = current_year - birth_year
    return age

# Calling the function
user_age = calculate_age()
print("Your age is:", user_age)

