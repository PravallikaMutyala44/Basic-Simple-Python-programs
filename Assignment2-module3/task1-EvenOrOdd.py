# Task 1: Check if a Number is Even or Odd (with exception handling)

try:
    # Take input from the user
    num = int(input("Enter a number: "))

    # Check if the number is even or odd
    if num % 2 == 0:
        print(num,"is an even number.")
    else:
        print(num, "is an odd number.")

except ValueError:
    print("Invalid input! Please enter an integer.")
