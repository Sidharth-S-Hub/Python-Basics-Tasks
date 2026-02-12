n = int(input("Enter a number: "))

even_count = 0
odd_count = 0
i = 1

while i <= n:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    i += 1

print("Even numbers count:", even_count)
print("Odd numbers count:", odd_count)
