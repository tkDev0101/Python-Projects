# print("hello")


# str = "this is a string"

# string = 'this is also a string'

# userInput = input("Type something: ")

# print(f"\nhere is the {userInput}")
# 1 != 2 #True

# elif is only allowed to be added after an "if statement"

# "not" operator reverses a condition

# i = 0
# while i <= 15:
#     print(i)
#     i += 3
#     # continue break


# while True:
#     sign = input("\nType an expression: "
#                    +"\n\t(+ - * / % **)"
#                    +"\n >> ")
    
#     if sign =="+" or sign =="-" or sign =="*" or sign =="/" or sign =="%" or sign =="**":
#         break  # Exit the loop after a valid choice
#     else:
#         print("\nPlease choose a Valid Mathimatical Expression.")
#         # The loop will repeat, asking the question again


    

# def get_number( number ):

#     while True:
#         operand = input(f"Number {number}: ")
#         try: 
#             return float(operand)
#         except:
#             print("Invalid number, try again")


# operand = get_number(1)


def validate_number():

    while True:
        numbers = input("\nSelect the Correct Number: ")
        try: 
            return float(numbers)
        except:
            print("Invalid number, try again")


numbers = validate_number()


