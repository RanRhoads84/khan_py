"""
Discover what the weight of an object would be on different planets.
This program calculates the weight of an object on different planets
based on its weight on Earth.
The program prompts the user to input the name of a planet
(Mars, Mercury, Venus, etc... ) and their weight on Earth.
It then calculates the weight of the object on the selected planet.

"""

# TODO: Add support for Saturn (9), Uranus (8.7), and Neptune (11).

planet_dict = {
    "Mars": 3.7,
    "Mercury": 3.7,
    "Venus": 8.9,
    "Jupiter": 23.1,
    "Saturn": 9.0,
    "Uranus": 8.7,
    "Neptune": 11.0,
}
# Prompt the user for a planet name.
planet = (
    input("Pick a planet in the solar: Mercury, Venus, etc...? "
          ).strip().capitalize()
)

# We measure a planet's gravitional force in m/s^2.
gravity = planet_dict.get(
    planet,
)
if gravity:
    print(f"The gravity on {planet} is {gravity} m/s^2.")
    # If the planet is not in the dictionary, gravity will be None.
elif planet == "Earth":
    print("Earth is where you live, so you don't need to know its gravity.")
elif planet == "Sun":
    print("The Sun is not a planet, it's a star.")
elif planet == "Moon":
    print("The Moon is not a planet, it's a natural satellite.")
elif planet == "Pluto":
    print("Pluto is not a planet, it's a dwarf planet. We demoted that fool!")
else:
    print("Unrecognized planet.")


if gravity:
    earth_weight = float(input("How much does it weigh on Earth (kg)? "))

    # An object's weight = mass * gravity.
    earth_gravity = 9.81
    mass = earth_weight / earth_gravity
    new_weight = round(mass * gravity, 1)

    print("It would weigh " + str(new_weight) + " kg on " + planet + ".")
