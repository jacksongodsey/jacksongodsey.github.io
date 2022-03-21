red = int(input())
green = int(input())
blue = int(input())

if red < (green and blue):
    green = green - red
    blue = blue - red
    red = red - red
elif green < (red and blue):
    blue = blue - green
    red = red - green
    green = green - green
elif blue < (red and green):
    red = red - blue
    green = green - blue
    blue = blue - blue
# this block is here just in case 255 comes up on every color    
elif (blue == red) and (red == green) and (blue == green) and (blue != 0):
    blue = blue - blue
    red = red - red
    green = green - green

print(f"{red} {green} {blue}")
