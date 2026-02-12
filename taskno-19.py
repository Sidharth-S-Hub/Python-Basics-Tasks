## Create a function that takes two numbers and returns their sum, difference, product, and quotient.(With arguments and return value)



def calculate_operations(num1, num2):
    sum_value = num1 + num2
    difference = num1 - num2
    product = num1 * num2
    
    if num2 != 0:
        quotient = num1 / num2
    else:
        quotient = "Cannot divide by zero"
    
    return sum_value, difference, product, quotient


# Calling the function
result = calculate_operations(10, 5)

print("Sum:", result[0])
print("Difference:", result[1])
print("Product:", result[2])
print("Quotient:", result[3])
