print('----------Python------------')

firstValue = float(input("Enter a number: "))
print('''
+
-
*
/
''')
operator = str(input("Enter any of the given operators for calculations: "))
secondValue = float(input("Enter a number: "))
result = 0

def calculation():
    if operator =="+":
        result = (firstValue + secondValue)
    elif operator =="-":
        result = (firstValue - secondValue)
    elif operator =="*":
        result = (firstValue * secondValue)
    elif operator =="/":
        result = (firstValue / secondValue)
    return result

close = False
while not close:
    moreCalculation = input(f"Do you want to do more calculation with the {calculation()}, 'Yes' or 'No': ")
    if moreCalculation.lower() =='no':
        close = True
        print(f"The result is: {calculation()}")
    else:
        firstValue = calculation()
        operator = input("Enter any of the given operators for calculations: ")
        secondValue = float(input("Enter a number: "))
        calculation()


# """By Angela Yu method"""

# def sum(a, b):
#     return a+b
# def sub(a, b):
#     return a-b
# def multiply(a, b):
#     return a*b
# def divide(a, b):
#     return a/b
# operation = {
#     '+': sum,
#     '-' : sub,
#     '*' : multiply,
#     '/'  :divide
# }


# num1 = int(input("Enter first number: "))
# for operator in operation:
#     print(operator)
# symbol = str(input("Enter the operation to perform"))
# num2 = int(input("Enter second number: "))

# calculation =operation[operator]
# result = calculation(num1, num2)
# print(f"{num1} {symbol} {num2} = {result}")
