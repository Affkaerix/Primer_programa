while True:
    print("Enter 'quit' to exit the program")
    print("Enter 'add' to addition a number")
    print("Enter 'substraction' to substract a number")
    print("Enter 'multiply' to multiply a number")
    print("Enter 'division' to divide a number")
    user_number = input(":")

    if user_number == "quit":
        break
    elif user_number == "add":
        num1 = float(input("Enter a number"))
        num2 = float(input("Enter a second number"))
        result = str(num1 + num2)
        print("The answer is " + result)
    elif user_number == "substraction":
        num1 = float(input("Enter a number"))
        num2 = float(input("Enter a second number"))
        result = str(num1 - num2)
        print("The answer is " + result)
    elif user_number == "multiply":
        num1 = float(input("Enter a number"))
        num2 = float(input("Enter a second number"))
        result = str(num1 * num2)
        print("The result is " + result)
    elif user_number == "divide":
        num1 = float(input("Enter a number"))
        num2 = float(input("Enter a second number"))
        result = str(num1 / num2)
        print("The result is " + result)
    else:
        print("Unknown input")
