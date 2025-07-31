def main():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2
        division = num1 / num2 if num2 != 0 else "Error: Division by zero"

        print("Addition:", addition)
        print("Subtraction:", subtraction)
        print("Multiplication:", multiplication)
        print("Division:", division)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
