name = input("Enter a name: ")
age = int(input("Enter an age: "))
color = input("Enter a color: ")
toy = input("Enter a toy: ")
print(name, "scolded the child,", '"You are', age, "years old, why are you eating a {} {}?".format(color, toy)) 
print("That shouldn't happen until you are {}.".format(age*2), ''"', sep='')
