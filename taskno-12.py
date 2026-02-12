 ## Write a Python program that:
##	Takes a number n as input
##   Uses a for loop to calculate the sum of numbers from 1 to n
##	Prints the result

n = int(input("Enter a number: "))
total = 0
for i in range(1, n + 1):
total += i
print("The sum from 1 to", n, "is:", total)