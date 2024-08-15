# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name  = l_name.title()
    
#     return f"{formated_f_name} {formated_l_name}"

# formatted_string = format_name(f_name="anGeLa", l_name="YU")

# print(formatted_string)

# *****************************************************************************************
# ******************************************************************************************

# def function_1(text):
#     return text + text


# def function_2(text):
#     return text.title()

# output = function_2(function_1("hello"))
# print(output)

# Functions with multiple return values

# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "Invalid Inputs"
#     formated_f_name = f_name.title()
#     formated_l_name  = l_name.title()
    
#     return f"{formated_f_name} {formated_l_name}"

# formatted_string = format_name(input("What is your first name?"), input("What is your last name?"))
                    
# print(formatted_string)

# ***************************************************************************************************************
# ********************************************************************************************************************

# LEAP YEAR USING FUNCTIONS

# Docstring

# def is_leap_year(year):
#     """ This is a function 
#         to check 
#         leap year """
        
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False

      
# output = is_leap_year(int(input("Enter the year: ")))
# print(output)

# ***************************************************************************************************************
# ***************************************************************************************************************

# ---------------------------------------------------------------------------------------
# THE CALCULATOR APP 
# ---------------------------------------------------------------------------------------
# TODO: Write out the functions - add, subtract, multiply, and divide.

import Day10_Project_The_Calculator_logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide (n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. keys = "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations. muultiply 4*8 using the dictionary.

# print(operations["+"](n1=4, n2=8)) #if we try to print only "+" then we get add in output

def calculator():
    print(Day10_Project_The_Calculator_logo.logo)
    should_repeat = True

    num1 = float(input("What is the first number?: ")) #Taking this output outside the loop so it doesnt get override

    while should_repeat:
        for symbol in operations:  #this because when we loop through the dict in onlt prints out the keys.
            print (symbol)
        operation_symbol = input("Pick an operation: ")

        num2 = float(input("What is the next number?: "))

        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")


        choice = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator: ").lower()
        if choice == "y":
            num1 = answer
        else:
            should_repeat = False
            print("\n" * 100)
            
            calculator()
            
            
calculator()           
        
        
