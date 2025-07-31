try:
    firstname = input("Enter your first name: ").strip()
    lastname = input("Enter your last name: ").strip()

    if not firstname or not lastname:
        raise ValueError("Both first and last names must be provided.")

    if not firstname.isalpha() or not lastname.isalpha():
        raise ValueError("Names should contain only alphabetic characters.")

    fullname = firstname + " " + lastname
    print(f"Hello, {fullname}! Welcome to the Python program.")


except ValueError as ve:
    print("Input Error:", ve)

except Exception as e:
    print("An unexpected error occurred:", e)
