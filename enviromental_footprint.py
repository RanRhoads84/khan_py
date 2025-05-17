'''
Takes user input to calculate their environmental footprint based on
their pets and transportation choices.
'''


footprint = 0

# ask the user how many days a week they commute to school or work
# and how they commute (foot, bike, bus, train, or car)

days = int(input("How many days a week do you commute to school or work? "))
# Check if the input is a valid number of days (1-7)
if 1 <= days <= 7 and days != 0:
    transport = input("Do you commute by foot, bike, bus, train, or car? "
                      ).strip().lower()

# Different methods of transportation have different environmental impacts.
    if transport == "car" and transport != 0:
        footprint = footprint + (8 * days)

    elif transport in ["bus", "train"]:
        footprint = footprint + (4 * days)
        print(footprint)
    elif transport in ['bike', 'foot']:
        footprint = footprint + days
else:
    transport = 0

# Ask the user if they have a pet.
has_pet = input("Do you have a pet (yes/no)? \n").strip().lower()[:1]
if has_pet == "y":
    footprint = footprint + 5
    eat_meat = input("Does it eat meat (yes/no)? \n").strip().lower()[:1]
    if eat_meat == "y":
        footprint = footprint + 10

# Calculate the environmental footprint based on the user's input.
print(f"Your environmental footprint score is {footprint}.")
