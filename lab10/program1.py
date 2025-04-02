def calculator():
    print("Simple Calculator")
    num1=float(input("Enter first number:"))
    num2=float(input("Enter second number:"))
    print("Select operations:")
    print("1.Add")
    print("2.Divide")
    print("3.Modulus")
    print("4.Exponent")
    print("5.Floor division")
    print("6.Subtraction")
    print("7.Multiplication")
    choice = input("Enter choice (1-5):")
    if choice=="1":
        print(f"{num1} + {num2}={num1+num2}")
    elif choice=="2":
        if num2!=0:
            print(f"{num1} / {num2}={num1/num2}")
        else:
            print("Error! Division by 0")
    elif choice=="3":
        print(f"{num1} % {num2}={num1%num2}")
    elif choice=="4":
        print(f"{num1} ** {num2}={num1**num2}")
    elif choice=="5":
        if num2!=0:
            print(f"{num1} // {num2}={num1//num2}")
        else:
            print("Error! Division by 0")
    elif choice=="6":
        print(f"{num1} - {num2}={num1-num2}")
    elif choice=="7":
        print(f"{num1} * {num2}={num1*num2}")
    else:
        print("Invalid Output")
calculator()
