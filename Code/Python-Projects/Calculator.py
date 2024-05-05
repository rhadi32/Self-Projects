# Author: Hadi Ramazani
# Date: Apr 30,2024
def calculate(n1, n2, op):
    if op == "+":
        result = n1+n2
    elif op == "-":
        result = n1-n2
    elif op == "*":
        result = n1*n2
    elif op == "/":
        result = n1/n2
    elif op == "^":
        result = n1**n2
    elif op == "**":
        result = n1**2

    else:
        raise ValueError("Invalid Operator")
    if result.is_integer():
        result = int(result)
    return result



continue_calculating = True
result = None

while continue_calculating:
    if result is None:
        number1 = float(input("Enter a number: "))
    else:
        number1 = result
    op = input("Select an operator (+, -, *, /, ^, **) or enter 'q' to quit: ")

    if op.lower() == 'q':
        break
    number2 = float(input("Enter another number: "))
    try:
        result = calculate(number1, number2, op)
        print('=', result)
    except ValueError as e:
        print(e)
        result = None
print("Calculator session ended.")
