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
    
    try:
        menu_option = int(input("\nType a Menu Option: "
                    + "\n1. Add Item"
                    + "\n2. View Items"
                    + "\n3. Something"
                    + "\n4. Exit"
                    + "\n\n\tYour Choice: "))

        if 1 <= menu_option <= 4:
            match menu_option:
                case 1:
                    print("Calling Add_Item_method()")
                    # Add_Item_method()  # Uncomment when method is defined
                    break  # Exit the loop

                case 2:
                    print("Calling View_Item_method()")
                    # View_Item_method()  # Uncomment when method is defined
                    break  # Exit the loop

                case 3:
                    print("Calling something_method()")
                    # something_method()  # Uncomment when method is defined
                    break  # Exit the loop

                case 4:
                    print("Exiting program...")
                    #Exit.environment()  # Uncomment if needed
                    break  # Exit the loop

        else:
            print("\nPlease choose a Valid Menu Option (1 - 4)")

    except ValueError:
        print("\nInvalid INPUT. Please enter a NUMBER! ")




