import math

wall_height = int(input('Enter wall height (feet):\n'))

wall_width = int(input('Enter wall width (feet):\n'))

wall_area = wall_width * wall_height

print(f'Wall area: {wall_area} square feet')

paint_needed = float(wall_area) / 350

print(f'Paint needed: {paint_needed:.2f} gallons')

cans_needed = math.ceil(paint_needed)

print(f'Cans needed: {cans_needed} can(s)')

print()

color = input('Choose a color to paint the wall:\n')

paint_prices = {
    'red': 35,
    'blue': 25,
    'green': 23
}

if color == 'red':
    print('Cost of purchasing {} paint: ${}'.format(color, (paint_prices['red'] * cans_needed)))

if color == 'blue':
    print('Cost of purchasing {} paint: ${}'.format(color, ((paint_prices['blue'] * cans_needed))))

if color == 'green':
    print('Cost of purchasing {} paint: ${}'.format(color, (paint_prices['green'] * cans_needed)))
