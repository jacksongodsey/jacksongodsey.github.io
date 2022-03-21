quarters = int(input("How many quarters: "))
dimes = int(input("How many dimes: "))
nickels = int(input("How many nickels: "))
pennies = int(input("How many pennies: "))
quartersvalue = quarters * 25
dimevalue = dimes * 10
nickelsvalue = nickels * 5
penniesvalue = pennies * 1
dollars = 100
money = quartersvalue + dimevalue + nickelsvalue + penniesvalue
if (money >=100):
    print("My money is: ${}".format(round(money/100, 2)))
else:
    print("My money is: ${} cents".format(money))