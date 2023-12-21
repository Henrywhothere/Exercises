

number1 = float(input("Enter first number: "))
number2 = float(input("Enter first number: "))


def add(number1, number2):
    result = number1 + number2
    return result

def subtract(number1, number2):
    result = number1 - number2
    return result

def multiple(number1, number2):
    result = number1*number2
    return result

def divide(number1, number2):
    result = number1/number2
    return result


print(''' + for addition
- for subtraction
* for multiplication
/ for division''')

operation = input("Enter the math operation you want: ")

if operation == '+':
    result = add(number1, number2)
    print("{} {} {} = {}".format(number1, operation, number2, result))
elif operation == '-':
    result = subtract(number1, number2)
    print("{} {} {} = {}".format(number1, operation, number2, result))
elif operation == '*':
    result = multiple(number1, number2)
    print("{} {} {} = {}".format(number1, operation, number2, result))
elif operation == '/':
    result = divide(number1, number2)
    print("{} {} {} = {}".format(number1, operation, number2, result))











    
