import json


#CONTACT LIST

# DATA STORAGE / DATA TYPES

def add_person():

    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {"name": name, "age": age, "email": email}

    return person




def display_people(people):
     for i, person in enumerate(people):
        # print(i + 1, "-", person["name"], "|" , person["age"], "|" , person["email"] )
        print(f'{i + 1} - {person["name"]} | {person["age"]} |  {person["email"]}' ) 



def delete_contact(people):

    display_people(people)
   
    while True:
        number = input("Enter a number to Delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of the Range!")
            else:
                break
        except:
            print("Invalid number, please enter a NUMBER")

    people.pop(number - 1)
    print("Person Deleted.")


def search(people):
    
    search_name = input("Search for a name: ")
    results = []

    for person in people:
        name = person['name']

        if search_name in name.lower():
            results.append(person)

    display_people(results)


    pass


print("\nWola, Welcome to the Contact Management System.")

with open("contacts.json", "r") as f:
    people = json.load(f) ["contacts"]

# people = [
#     {"name": "Tom", "age": 74, "email": "tom@mail.com"},
#     {"name": "Ron", "age": 42, "email": "ron@mail.com"},
#     {"name": "Don", "age": 32, "email": "don@mail.com"},
#     {"name": "John", "age": 92, "email": "john@mail.com"},

# ]

while True:
    print("\nContact List Size: ", len(people))
    command = input("\nYou can 'Add', 'Delete' or 'Search' and 'Q' for quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added!")

    elif command == "delete":
        delete_contact(people)

    elif command == "search":
        search(people)
    
    elif command == "q":
        break
    else:
        print("Invalid command.")


with open("contacts.json", "w") as f:
    json.dump( {"contacts": people}, f)
    # people = json.load(f) ["contacts"]