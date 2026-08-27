def calculator():
    try:
        number1 = int(input("enter the first number :"))
        operation = input("Select an operation (+, -, *, /):")
        number2 = int(input("enter the second number :"))

        if operation == '+':
            result = number1 + number2
        elif operation == '-':
            result = number1 - number2
        elif operation == '*':
            result = number1 * number2
        elif operation == '/':
            result = number1 / number2
        else:
            return "Invalid operation"
    except ValueError:
        return "Please enter whole numbers only."
    except ZeroDivisionError:
        return "You cannot divide by zero."

    return f"{number1} {operation} {number2} = {result}"

print(calculator())

again = input("Do you want to calculate again? (yes/no): ")
while again == "yes":
    print(calculator())
    again = input("Do you want to calculate again? (yes/no): ")
    if again == "no":
        print("Thank you for using the calculator!")
        break

