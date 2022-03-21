highway_number = int(input())

if ((highway_number % 2) == 0) and (1 <= highway_number < 100):
    print(f"I-{highway_number} is primary, going east/west.")
elif ((highway_number % 2) != 0) and (1 <= highway_number < 100):
    print(f"I-{highway_number} is primary, going north/south.")
elif ((highway_number % 2) == 0) and (999 >= highway_number >= 100) and (highway_number != 200):
    print(f"I-{highway_number} is auxiliary, serving I-{highway_number % 100}, going east/west.")
elif ((highway_number % 2) != 0) and (999 >= highway_number >= 100) and (highway_number != 200):
    print(f"I-{highway_number} is auxiliary, serving I-{highway_number % 100}, going north/south.")
else:
    print(f"{highway_number} is not a valid interstate highway number.")
