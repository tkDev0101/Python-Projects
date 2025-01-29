
#Housekeping - get user data

name = input("Wassup, Wusyaname your name: ")
print(f"Welcome to the Party, Mr. {name}")

should_we_play = input("Do you want to play? ").lower()
play = should_we_play == "yes" or should_we_play == "y"

if play:
    print("\nWoo! \nWe're about to have some real good fun, ya feel!")


    weapon_choice = input("Wait, wat weapon you packing?" + 
                            "\n1. Glock" +
                            "\n2. Knife" +
                            "\n3. Axe" + 
                            "\n4. Shotgun" +
                            "\nYour choice: ")

    match weapon_choice:
        case 1:
            weapon = "Glock"

        case 2:
            weapon = "Knife"

        case 3:
            weapon = "Axe"

        case 4:
            weapon = "Shotgun"

        case _:
            print("Ayt, it's you and the Almighty then.")

            
            while True:
                direction = input("Do you want to go left or right? \n").lower()

                if direction == "left":
                    print("We heading to the left")
                    choice = input("Okay, you's see's a bridge, now is you gonna swim under it or cross it? \n\t(swim/cross) \n")

                    if choice == "swim":
                        print("You Dummy, you can't swim, now drown cuz")
                    elif choice == "cross":
                        print("Good job ma brother, you found the gold neck piece!")
                    break  # Exit the loop after a valid choice

                elif direction == "right":
                    print("Wrong choice my guy, now I'ma have to cap ypur a$$!!")
                    break  # Exit the loop after a valid choice
                else:
                    print("Nah Blud, it's either you're coming or you going")
                    # The loop will repeat, asking the question again

else:
    print("Ayt, we gon run it back next time!")