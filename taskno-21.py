##Write a Python program that:
	##	Uses variables to store student name and number of subjects
	##	Uses a function to calculate total and average marks
	##	Uses a loop to read marks for each subject
	##	Uses if–else to decide the grade
##Grade Rules
	##	Average ≥ 75 → Distinction
	##	Average ≥ 50 → Pass
	##	Else → Fail

#         store student details
student_name = input("Enter student name: ")
num_subjects = int(input("Enter number of subjects: "))

#   Function to calculate total and average marks
def calculate_total_and_average(n):
    total = 0

    #Loop to read marks
    for i in range(1, n + 1):
        marks = int(input(f"Enter marks for subject {i}: "))
        total += marks

    average = total / n
    return total, average

# Function call
total_marks, avg_marks = calculate_total_and_average(num_subjects)

# 4. If–else to decide grade
if avg_marks >= 75:
    grade = "Distinction"
elif avg_marks >= 50:
    grade = "Pass"
else:
    grade = "Fail"


print("Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", avg_marks)
print("Grade:", grade)
