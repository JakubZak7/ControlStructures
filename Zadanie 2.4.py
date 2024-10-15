number1 = int(input("Type first number: "))
number2 = int(input("Type second number: "))
operator = input("Select a operator: ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "/":
    result = number1 / number2
elif operator == "*":
    result = number1 * number2
else:
    print("Type correct operator")

print(f"{number1} {operator} {number2} = {result}")