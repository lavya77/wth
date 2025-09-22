print("Welcome to the Smart Calculator!")
print("You can enter expressions like 5 + 3 * 2 or (2 ** 3) % 3")

while True:
    expr = input("\nEnter expression: ")

    try:
        result = eval(expr)
        print(f"Result: {expr} = {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception:
        print("Error: Invalid expression!")

    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != 'yes':
        print("Exiting calculator. Goodbye!")
        break
