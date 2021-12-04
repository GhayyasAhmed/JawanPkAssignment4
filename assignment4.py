

# Program 1
# print("Enter what operation you want to perform: ")
# operators = ["+", "-", "*", "/", "**"]
# operator = input("Addition(+), Subtraction(-), Multiplication(*), Division(/), Power(**): ")
#
# if operator in operators:
#     num1 = float(input("Enter number 1: "))
#
#     num2 = float(input("Enter number 2: "))
#
#     if operator == "+":
#         res = num1 + num2
#         print(num1,"+",num2,"=",res)
#
#     elif operator == "-":
#         res = num1 - num2
#         print(num1,"-",num2,"=",res)
#
#     elif operator == "*":
#         res = num1 * num2
#         print(num1,"*",num2,"=",res)
#
#     elif operator == "/":
#         res = num1 / num2
#         print(num1,"/",num2,"=",res)
#
#     elif operator == "**":
#         res = num1 ** num2
#         print(num1,"**",num2,"=",res)
#
# else:
#     print("Invalid operator")


# Program 2

# lst = ["Ghayyas", "Ahmed", "JawanPk", 14, "Student", 2021]
# flag = True
# for i in lst:
#     if type(i) == int or type(i) == float:
#         print("Yes there is atleast one number in the list")
#         flag = False
#         break
#
# if flag:
#     print("There isn't any number in the list")

# Program 3

# dict1 = {"Name":"Ghayyas", "Year": 2021}
# print(dict1)
# # Add key age without value using None
# dict1["Age"] = None
# print(dict1)


# Program 4

# dict2 = {"Name": "Ghayyas", 1: 1, 2:2, 3:3}
# numericSum = 0
# for i in dict2.items():
#     for j in i:
#         if type(j) == int or type(j) == float:
#             numericSum += j
#
# print("Sum of numeric items in dict =", numericSum)
#
