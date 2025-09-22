def calc():
    while True:
        num1 = float(input("Enter a number: "))
        operator = input(''' 
Enter + for addition
Enter * for multiplication
Enter - for subtraction
Enter / for division
Enter ** for power
Enter % for remainder
Enter operator: ''')
        num2 = float(input("Enter second number: "))

        if operator == '+':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif operator == '*':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif operator == '-':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif operator == '**':
            print(f"Result: {num1} ** {num2} = {num1 ** num2}")
        elif operator == '%':
            print(f"Result: {num1} % {num2} = {num1 % num2}")
        elif operator == '/':
            if num2 == 0:
                print("Can't divide by zero!")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operator!")

        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting calculator. Goodbye!")
            break

calc()
