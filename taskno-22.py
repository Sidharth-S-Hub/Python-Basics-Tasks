##Write a Python program that:
	#1.	Uses variables to store account balance
	#2.	Uses a function to handle withdrawal
	##3.	Uses a loop to allow multiple attempts
	##4.	Uses if–else to validate withdrawal amount
##Rules
	##•	Initial balance = 5000
	##	User gets 3 attempts
	##	Withdrawal amount must be:
	##	Less than or equal to balance
	##	Greater than 0



##Variable to store account balance
balance = 5000

##Function to handle withdrawal
def withdraw(amount):
    global balance
    
    # 4. If–else to validate withdrawal amount
    if amount > 0 and amount <= balance:
        balance -= amount
        print("Withdrawal successful!")
        print("Remaining Balance:", balance)
    else:
        print("Invalid amount! Please try again.")

##3p to allow 3 attempts
attempts = 3

while attempts > 0:
    print("\nCurrent Balance:", balance)
    amount = float(input("Enter withdrawal amount: "))
    
    withdraw(amount)
    
    attempts -= 1
    print("Attempts left:", attempts)

print("\nTransaction session ended.")
