import math
from math import *

first_num = input("Enter the first number: ")
operation = input("Choose the operation:\n1_ +\n2_ -\n3_ *\n4_ /\n5_ ^\n6_ %\n")
second_num = input("Enter the second number: ")

result = ""

if first_num.isdigit() and second_num.isdigit():
    num1 = float(first_num)
    num2 = float(second_num)
    if operation == "+" or operation == "1":
        result = num1 + num2
        print(f"The result = {result}")
    elif operation == "-" or operation == "2":
        result = num1 - num2
        print(f"The result = {result}")
    elif operation == "*" or operation == "3":
        result = num1 * num2
        print(f"The result = {result}")
    elif operation == "/" or operation == "4":
        result = num1 / num2
        print(f"The result = {result}")
    elif operation == "^" or operation == "5":
        result = num1 ^ num2
        print(f"The result = {result}")
    elif operation == "%" or operation == "6":
        result = num1 % num2
        print(f"The result = {result}")
    else:
        print("Invalid operation!")
else:
    print("Enter a valid number!")
    exit()

choice = input("1-round or floor or ceiling\n2-number without decimal point\n3-Exit\n")
final_result = 0

if choice == "round":
    final_result = round(result)
elif choice == "floor":
    final_result = math.floor(result)
elif choice == "ceiling":
    final_result = math.ceil(result)
elif choice == "number without decimal point" or choice == "2":
    final_result = int(result)
elif choice == "Exit" or choice == "3":
    pass
else:
    print("Error!")

print(f"The final result = {final_result}")

