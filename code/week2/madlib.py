adj = input("List an adjective to describe the world: ")
favorite_thing = input("What is your favorite thing about the world: ")
required_orbit_time = "365"

while True:
    orbit_time = input("Enter the amount of days it takes the Earth to orbit the\
 Sun:\n")
    if orbit_time == required_orbit_time:
        break
    else:
        print("Wrong amount of days please try again")
madlib = f"The world is so {adj}! It orbits the Sun every {orbit_time} days! \
The thing I love most about the world is {favorite_thing}!"

print(madlib)
