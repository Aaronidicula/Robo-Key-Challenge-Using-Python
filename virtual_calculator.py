'''
This is an virtual simple calculator. with provision to handle all the errors. without breaking the code.
created by Aaron Idicula.
'''
try:
    nums_1 = int(input("Enter first integer: "))
    nums_2 = int(input("Enter second integer: "))
    operator = input("Enter an operator from this list (+,-,*,/) : ")
    #Enter an operator
    if operator == "+":
        print(nums_1 + nums_2)
    elif operator == "-":
        print(nums_1 - nums_2)
    elif operator == "*":
        print(nums_1 * nums_2)
    elif operator == "/":
        print(nums_1/nums_2)
except ZeroDivisionError as zerr:
    print(zerr)
except ArithmeticError as aerr:
    print(aerr)
except ValueError:
    print("Invalid Input!")
