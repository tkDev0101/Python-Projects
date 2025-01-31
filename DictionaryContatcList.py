import json  # Importing JSON module to handle reading/writing contact data in a JSON file

# ------------------------ CONTACT MANAGEMENT SYSTEM ------------------------

print("\nWola, Welcome to the Contact Management System.")  # Greeting message

# Load contacts from the JSON file if available
with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]  # Extract the list of contacts

# # Example contact list (used as a backup)
# people = [
#     {"name": "Tom", "age": 74, "email": "tom@mail.com"},
#     {"name": "Ron", "age": 42, "email": "ron@mail.com"},
#     {"name": "Don", "age": 32, "email": "don@mail.com"},
#     {"name": "John", "age": 92, "email": "john@mail.com"},
# ]

# ------------------------ FUNCTIONS ------------------------

# Function to add a new person to the contact list
def add_person():
    name = input("Name: ")  # Get the name input from the user
    age = input("Age: ")  # Get the age input
    email = input("Email: ")  # Get the email input

    # Create a dictionary to store the contact details
    person = {"name": name, "age": age, "email": email}

    return person  # Return the newly created contact


# Function to display all contacts in a formatted manner
def display_people(people):
    for i, person in enumerate(people):  # Iterate through the contact list
        print(f'{i + 1} - {person["name"]} | {person["age"]} | {person["email"]}')  # Display each contact


# Function to delete a contact from the list
def delete_contact(people):
    display_people(people)  # Show available contacts before deleting

    while True:  # Keep asking until a valid number is entered
        number = input("Enter a number to Delete: ")  # Ask the user for the contact number to delete
        try:
            number = int(number)  # Convert input to an integer
            if number <= 0 or number > len(people):  # Check if the number is out of range
                print("Invalid number, out of the Range!")
            else:
                break  # Exit the loop if a valid number is entered
        except:
            print("Invalid number, please enter a NUMBER")  # Handle non-numeric input

    people.pop(number - 1)  # Remove the selected contact (adjust for zero-based index)
    print("Person Deleted.")  # Confirm deletion


# Function to search for a contact by name
def search(people):
    search_name = input("Search for a name: ").lower()  # Get search input (convert to lowercase)
    results = []  # List to store matching contacts

    for person in people:  # Iterate over all contacts
        name = person['name'].lower()  # Convert contact name to lowercase for case-insensitive search
        if search_name in name:  # Check if the search query matches part of the name
            results.append(person)  # Add matching contact to the results list

    display_people(results)  # Display the found contacts


# ------------------------ MAIN PROGRAM LOOP ------------------------

while True:
    print("\nContact List Size: ", len(people))  # Show the number of contacts available
    command = input("\nYou can 'Add', 'Delete' or 'Search' and 'Q' for quit: ").lower()  # Get user command

    if command == "add":
        person = add_person()  # Call add_person() to create a new contact
        people.append(person)  # Add the new contact to the list
        print("Person added!")  # Confirm addition

    elif command == "delete":
        delete_contact(people)  # Call delete_contact() to remove a contact

    elif command == "search":
        search(people)  # Call search() to find a contact by name

    elif command == "q":
        break  # Exit the program loop

    else:
        print("Invalid command.")  # Handle incorrect input

# ------------------------ SAVE CONTACTS TO FILE ------------------------

# Write updated contacts back to the JSON file for data persistence
with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)  # Store the updated contact list in JSON format
