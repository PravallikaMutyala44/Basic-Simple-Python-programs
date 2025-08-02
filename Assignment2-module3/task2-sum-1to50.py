# Task 2: Sum of Integers from 1 to 50 Using a Loop (with exception handling)

try:
    # Initialize sum
    total = 0

    # Use for loop from 1 to 50
    for i in range(1, 51):
        total += i

    # Display the final sum
    print("The sum of numbers from 1 to 50 is:", total)

except Exception as e:
    print("An error occurred:", e)
