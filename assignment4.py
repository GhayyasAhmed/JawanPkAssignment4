

# Program 1
print("Enter what operation you want to perform: ")
operators = ["+", "-", "*", "/", "**"]
operator = input("Addition(+), Subtraction(-), Multiplication(*), Division(/), Power(**): ")

if operator in operators:
    num1 = float(input("Enter number 1: "))

    num2 = float(input("Enter number 2: "))

    if operator == "+":
        res = num1 + num2
        print(num1,"+",num2,"=",res)

    elif operator == "-":
        res = num1 - num2
        print(num1,"-",num2,"=",res)

    elif operator == "*":
        res = num1 * num2
        print(num1,"*",num2,"=",res)

    elif operator == "/":
        res = num1 / num2
        print(num1,"/",num2,"=",res)

    elif operator == "**":
        res = num1 ** num2
        print(num1,"**",num2,"=",res)

else:
    print("Invalid operator")
