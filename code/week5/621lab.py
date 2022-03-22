service_dict = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}

print(f"Davy's auto shop services\n" 
        + f"Oil change -- ${service_dict['Oil change']}\n" 
        + f"Tire rotation -- ${service_dict['Tire rotation']}\n" 
        + f"Car wash -- ${service_dict['Car wash']}\n"
        + f"Car wax -- ${service_dict['Car wax']}")

print()

first_service = input("Select first service:\n")
second_service = input("Select second service:\n")

print()
print("Davy's auto shop invoice")
print()

if first_service in service_dict:
    print(f"Service 1: {first_service}, ${service_dict[first_service]}")
    first_service = service_dict[first_service]
elif first_service == '-':
    print("Service 1: No service")
    first_service = 0

if second_service in service_dict:
    print(f"Service 2: {second_service}, ${service_dict[second_service]}")
    second_service = service_dict[second_service]
elif second_service == '-':
    print("Service 2: No service")
    second_service = 0

total = int(first_service) + int(second_service) 

print()
print(f"Total: ${total}")
    
