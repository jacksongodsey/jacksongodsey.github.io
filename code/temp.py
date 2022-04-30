import first

def one(number):
    return number ** 2

def two(number):
    return number * 8

def three(number):
    return one(number) - two(number)

print(three(9))
print(first.three(9))
print(first.four(9))
