
#TEXT BASED Calculator 
print("\nWelcome to the calculator app! \n")


def get_number( number ):
        
    while True:
        operand = input(f"Number {number}: ")
        try: 
            return float(operand)
        except:
            print("Invalid number, try again")


operand = get_number(1)
operand2 = get_number(2)


while True:
    sign = input("\nType an expression: "
                   +"\n\t(+ - * / % **)"
                   +"\n >> ")
    
    if sign =="+" or sign =="-" or sign =="*" or sign =="/" or sign =="%" or sign =="**":
        break  # Exit the loop after a valid choice
    else:
        print("\nPlease choose a Valid Mathimatical Expression.")
        # The loop will repeat, asking the question again

result = 0

if sign == "+":
    result = operand + operand2
elif sign == "-":
    result = operand - operand2
elif sign == "*":
    result = operand * operand
elif sign == "/":
    if operand2 != 0:
        result = operand / operand2
    else:
        print("Division by Zero.")


print(f"Answer: {result}")

