service_dict = {'oil change': 35, 'tire rotation': 19, 'car wash': 7}

desired_auto = input("Enter desired auto service:\n")
print(f"You entered: {desired_auto}")

desired_auto = desired_auto.lower()

if desired_auto in service_dict:
    print(f"Cost of {desired_auto}: ${service_dict[desired_auto]}") 
else:
    print("Error: Requested service is not recognized")
