"""To build a calculator
"""

op_list = ['+', '-', '*', '/']

def operation_list():
    for op in op_list:
        print(op)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def division(a, b):
    return a / b

calculator_dict = {"+":add,
                   "-":subtract,
                   "*":multiply,
                   "/":division
                   }

result = 0
reserve_option = 'n'
should_continue = True
while should_continue:
    if reserve_option == 'n':
        first_number = int(input("What's the first number?: "))
    operation_list()
    
    op_input = input("Pick an operation from the above operation list: ")
    second_number = int(input("What's the second number?: "))
    
    for key in calculator_dict:
        if key == op_input:
           result = calculator_dict[key](first_number, second_number)
           print(f"{first_number} {key} {second_number} = {result}")
           break
    
    should_continue = input("Do you want to continue using the calculator? Type 'yes' to continue, otherwise 'no' to exit:")
    if should_continue == 'yes':
        should_continue = True
    else:
        print('Goodbye')
        break 
    
    reserve_option = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if reserve_option == 'y':
        first_number = result
     