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




menu_option = 0

while True:
    print("\n**WELCOME TO MAIN MENU**")
    int(menu_option = input("\nType an expression: "
                +"\n1. Add Item"
                +"\n2. View Items"
                +"\n3. Something"
                +"\n4. Exit"
                +"\n\n\tYour Chioce: "))
    
    if 1 >= menu_option <= 4:
        match menu_option:
            case 1:
                call_method = "Add_Item_method()"

            case 2:
                call_method = "View_Item_method()"

            case 3:
                call_method = "something_method()"

            case 4:
                call_method = "Exit.environment()"

            case _:
                print("Ayt, it's you and the Almighty then.")

                break  # Exit the loop after a valid choice
    else:
        print("\nPlease choose a Valid Menu Option (1 - 4)")
        # The loop will repeat, asking the question again


        
print(call_method)







# def get_number( number ):

#     while True:
#         operand = input(f"Number {number}: ")
#         try: 
#             return float(operand)
#         except:
#             print("Invalid number, try again")


# operand = get_number(1)

