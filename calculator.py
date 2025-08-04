num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num1 = float(num1)
num2 = float(num2)

op = input("Enter +, -, * or /: ")


if op == "+":
    answer = num1 + num2
    print("The answer is", answer)
elif op == "-":
    answer = num1 - num2
    print("The answer is", answer)
elif op == "*":
    answer = num1 * num2
    print("The answer is", answer)
elif op == "/":
    if num2 != 0:
        answer = num1 / num2
        print("The answer is", answer)
    else:
        print("You can't divide by 0")
else:
    print("Invalid operation")
