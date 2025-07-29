num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))
print("Choose operation: +  -  *  /")
op = input("Enter operator: ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")
