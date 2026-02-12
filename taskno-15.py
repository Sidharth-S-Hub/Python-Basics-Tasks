##   Code a system that allows a user 5 login attempts:
	##	If the user enters empty input, skip that attempt (continue)
	##	If the user enters the correct password, stop immediately (break)
	##	Otherwise, allow the next attempt



correct_password = "admin123"

for attempt in range(1, 6):   # 5 attempts
    password = input("Enter password: ")

    if password == "":
        print("Empty input! Try again.")
        continue   # Skip this attempt

    if password == correct_password:
        print("Login successful!")
        break   # Stop immediately

    else:
        print("Wrong password!")

else:
    print("All 5 attempts used. Access denied.")
