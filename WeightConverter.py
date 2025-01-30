
def validate_weight():

    while True:
        weight = input("\nEnter your weight: ")
        try: 
            return float(weight)
        except:
            print("Invalid number, try again")


weight = validate_weight()
# weight = float(input("\nEnter your weight: "))
unit = input("Kilograms or Pounds? (kg or lb): ").lower()

if unit == "kg":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"\n **Your Weight is: { round(weight, 2) } {unit} **")
elif unit == "lb":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"\n **Your Weight is: { round(weight, 2) } {unit} **")
else:
    print(f"{unit} was not valid")
    
    




