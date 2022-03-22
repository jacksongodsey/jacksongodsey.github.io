user_input = 'Gertrude Sam Ann Joeseph'# input()
short_names = user_input.split()

short_names.pop(0)
short_names[2] = 'Joe'

print(short_names)