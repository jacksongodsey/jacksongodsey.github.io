'''
Question 1:

first_number = int(input())
second_number = int(input())

if first_number > second_number:
    print("greater than")
elif first_number == second_number:
    print("equal to")
elif first_number < second_number:
    print("less than")
else:
    print("you did not enter any number i can make sense of. not sure how you got to here")
'''

'''
Question 2:

first_name = 'Jackson'
last_name = 'Godsey'

quiz_1 = 83
quiz_2 = 95
quiz_3 = 79
score = (quiz_1 + quiz_2 + quiz_3) / 3

print('First Name   Last Name   Quiz 1 Score   Quiz 2 Score   Quiz 3 Score   Average Score')
print(f'{first_name:<12} {last_name:<10} {quiz_1:^14} {quiz_2:^14} {quiz_3:^14} {score:>14.1f}')
'''


'''
Question 3:

quiz_score = int(input())
final_exam_score = int(input())

final_weight = .3
quiz_weight = .7

final_score = (final_exam_score * final_weight) + (quiz_score * quiz_weight)

if final_score > final_exam_score + 10:
    final_exam_score += 10

print("The calculated final score was {:3.1f} and the adjusted final score was {:3.1f}".format(final_score, final_exam_score))
'''
'''
Question 4:

def gettemp():
    temperature = int(input())
    if temperature > 90 or temperature < 20:
        print("Please enter a valid number between 20 and 90")
        return 0
    elif temperature > 70:
        print("it is hot today")
    elif temperature > 40:
        print("it is cool today")
    elif temperature > 19:
        print("it is cold today")

answer = gettemp()
if answer == 0: gettemp()
'''
'''
Question 5:

lengthdata = []
heightdata = []
widthdata = []
volumedata = []

for i in range(3):
    lengthdata.append(int(input()))
    heightdata.append(int(input()))
    widthdata.append(int(input()))

for j in range(3):
    volumedata.append(lengthdata[i] * heightdata[i] * widthdata[i])

print('\n\nLength  Width  Height  Volume')
for i in range(3):
    print(f'{lengthdata[i]:6} {widthdata[i]:6} {heightdata[i]:6} {volumedata[i]:6}')
'''

'''
Question 6:

number_list = []
sum = 0
size = int(input("Enter how big you want the list to be: "))
count = 0
for i in range(size):
    number_list.append(int(input("Enter a number to put in the list: ")))
    sum += number_list[i]
    count += 1

median = int(size/2)

average = sum/count
number_list.sort()
print(f"{sum:5} {count:5} {average:5.1f} {number_list[median]:5}")
'''

'''
Question 7:

sum = 0
while sum < 100:
    current = int(input("Please enter a number to add to the total: "))
    sum += current
    if sum <= 100:
        print(f"{current}")
    else:
        print(f"the sum of 100 or more was found on {current}")
'''

'''
def sum(num1, num2):
    total = num1 + num2
    return total

num1 = float(input())
num2 = float(input())

print(f"Sum of {num1} and {num2} is {sum(num1, num2)}")
'''