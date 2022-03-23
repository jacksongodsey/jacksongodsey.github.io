# midterm2

- [midterm2](#midterm2)
  - [Links to important documents](#links-to-important-documents)
    - [Question 1:](#question-1)
    - [Question 2:](#question-2)
    - [Question 3:](#question-3)
    - [Question 4:](#question-4)
    - [Question 5:](#question-5)
    - [Question 6:](#question-6)
    - [Question 7:](#question-7)
    - [Question 8:](#question-8)

## Links to important documents
Here is a link to the powerpoint that contains the questions I was solving for in pdf format should you want it. [midterm2 pdf](../assets/midterm2.pdf)

Here is the link to the python file that contains the code I wrote to solve these questions. It will also be written in source blocks below.
[midterm2.py](../code/midterm2.py)

### Question 1:

Input two numbers. Determine whether the first number is greater than, equal to, or less than the second number.

My Answer:

```python
if first_number > second_number:
    print("greater than")
elif first_number == second_number:
    print("equal to")
elif first_number < second_number:
    print("less than")
else:
    print("you did not enter any number i can make sense of. not sure how you got to here")
```

### Question 2:

Identify variables that hold a first name that you make up, a last name that you make up, and three quiz scores that you make up. Create a table that has titles over each variable and displays the first and last names aligned left, the three quiz scores aligned center, and the average quiz score aligned right with one decimal place.

My Answer:

```python
first_name = 'Jackson'
last_name = 'Godsey'

quiz_1 = 83
quiz_2 = 95
quiz_3 = 79
score = (quiz_1 + quiz_2 + quiz_3) / 3

print('First Name   Last Name   Quiz 1 Score   Quiz 2 Score   Quiz 3 Score   Average Score')
print(f'{first_name:<12} {last_name:<10} {quiz_1:^14} {quiz_2:^14} {quiz_3:^14} {score:>14.1f}')
```

### Question 3:

Write a program where a quiz average score is input and a final exam score is input. Award the final grade based on a weighting of 30% is the final exam score and 70% is the quiz average score. However, the final grade cannot be more than 10% higher than the final exam grade.

My Answer:

```python
quiz_score = int(input())
final_exam_score = int(input())

final_weight = .3
quiz_weight = .7

final_score = (final_exam_score * final_weight) + (quiz_score * quiz_weight)

if final_score > final_exam_score + 10:
    final_exam_score += 10

print("The calculated final score was {:3.1f} and the adjusted final score was {:3.1f}".format(final_score, final_exam_score))
```
### Question 4:

Write a program that accepts a temperature. The temperature must be between 20 and 90. If the temperature is between 20 and 40 the print is “cold”. If the temperature is between 41 and 70, the output is “cool”. If the temperature is between 71 and 90, the temperature is “hot”

My answer:

```python
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
```

### Question 5:

Input the length, width, and height for three different shapes into three lists; one for length, one for width, and one for height. Use a ‘for’ loop to create the inputs. Create a table that shows the length, width and height for each shape plus its volume. Display the numbers in each column so the ones place for each column is vertically aligned

My Answer:

```python
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
```
### Question 6:

Create a list of numbers that you determine. Input the number of entries first (choose an odd number) and then populate the list. Once the list is made, find the sum, count, average, and median value in the list.

My Answer:

```python
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
```

### Question 7:

Enter a number until the sum of the numbers entered is more than 99. Print each number as you enter them if they are under 100 and print “The sum of 100 or more was found on xx”.

My Answer:

```python
sum = 0
while sum < 100:
    current = int(input("Please enter a number to add to the total: "))
    sum += current
    if sum <= 100:
        print(f"{current}")
    else:
        print(f"the sum of 100 or more was found on {current}")
```

### Question 8:

Pass two numbers into a function. Add those two numbers together and return the sum back to the program where you will print the sum out.

My Answer:

```python
def sum(num1, num2):
    total = num1 + num2
    return total

num1 = float(input())
num2 = float(input())

print(f"Sum of {num1} and {num2} is {sum(num1, num2)}")
```