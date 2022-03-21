year = int(input())

is_leap_year = False

is_leap_year = True if ((year % 4) == 0) and ((year % 400) % 16 == 0) else False

print(f"{year} - leap year") if is_leap_year == True else print(f"{year} - not a leap year")

