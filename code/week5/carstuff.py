car_year = int(input())

if car_year < 1967:
    print("Probably has few safety features.")

if (car_year > 1969) and (car_year <= 1992):
    print("Probably has seat belts.")

if (car_year > 1992) and (car_year <= 2000):
    print("Probably has seat belts.")
    print("Probably has electronic stability control.")

if car_year > 2000:
    print("Probably has seat belts.")
    print("Probably has electronic stability control.")
    print("Probably has tire-pressure monitor.")

