total_change = int(input())


if total_change < 1:
    print("No change")

def printChange(total_change):
    dollar = total_change // 100
    dollar_change = total_change % 100
    if dollar == 1:
        print(f"{dollar} Dollar")
        printChange(total_change - 1 * 100)
    elif dollar > 1:
        print(f"{dollar} Dollars")
        printChange(total_change - dollar * 100)
    elif dollar_change >= 25:
        quarter = dollar_change // 25
        if quarter == 1:
            print(f"{quarter} Quarter")
            printChange(total_change - 1 * 25)
        elif quarter > 1:
            print(f"{quarter} Quarters")
            printChange(total_change - quarter * 25)
    elif dollar_change >= 10:
        dime = dollar_change // 10
        if dime == 1:
            print(f"{dime} Dime")
            printChange(total_change - 1 * 10)
        elif dime > 1:
            print(f"{dime} Dimes")
            printChange(total_change - dime * 10)
    elif dollar_change >= 5:
        nickel = dollar_change // 5
        if nickel == 1:
            print(f"{nickel} Nickel")
            printChange(total_change - 1 * 5)
        elif nickel > 1:
            print(f"{nickel} Nickels")
            printChange(total_change - nickel * 5)
    elif dollar_change >= 1:
        penny = dollar_change // 1
        if penny == 1:
            print(f"{penny} Penny")
            printChange(total_change - 1 * 1)
        else:
            print(f"{penny} Pennies")
            printChange(total_change - penny * 1)
    elif dollar_change == 0:
        return



printChange(total_change)

