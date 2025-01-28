
print("\n A simple ARITHMETIC Calculator: \n")
operator = input("Please Enter an Operaor (+ - * /): ")
num1 = float(input("Enter the 1st Number: "))
num2 = float(input("Enter the 2nd Number: "))

if operator == "+":
    answer = num1 + num2
    print(round(answer, 3))   #rouund off to 3 decimal places
elif operator == "-":
    answer = num1 - num2
    print(round(answer, 3))
elif operator == "*":
    answer = num1 * num2
    print(round(answer, 3))
elif operator == "/":
    answer = num1 / num2
    print(round(answer, 3))

else: #
    print(f"{operator} is not a valid operator")



