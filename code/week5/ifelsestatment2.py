user_num1 = int(input())
user_num2 = int(input())

if user_num1 < 0:
    print("user_num1 is negative.")

if user_num2 > 10:
    user_num2 = 4
else:
    print("user_num2 is less than or equal to 10.")

print('user_num2 is', user_num2)
