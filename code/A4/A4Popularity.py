###########
#   Jackson Godsey
#   Assignment 4
#   04/18/2022
#
#   Description: This program allows the user to play a game and guess if either a boy or girl's name was more popular in 2015.
#   Inputs: Two text files with the names, births, and rank of each name. It also asks for user input for their guess and wether or not they would like to play again.
#   Outputs: How many questions the user answered and how many they got right.
###########

import boysclass
import girlsclass
import random


def create_boy_list():
    """
    Description: This function creates a list of class objects that include the rank, name, and births of each of the boy names in the text file.
    Inputs: This function takes no input, but it does read from a text file.
    Returned value: This function returns a list of class objects.
    Preconditions: This function requires that a text file with the below name exists, and is in a correct format.
    """
    contents = boys.read()
    boys.close()
    boy_names = contents.split("\n")
    boy_list = []
    for x in boy_names:
        x = x.split()
        name = str(x[1])
        name = boysclass.bnames(x[0], x[1], x[2])
        boy_list.append(name)
        name = ""
    return boy_list


def create_girl_list():
    """
    Description: This function creates a list of class objects that include the rank, name, and births of each of the girl names in the text file.
    Inputs: This function takes no input, but it does read from a text file.
    Returned value: This function returns a list of class objects.
    Preconditions: This function requires that a text file with the below name exists, and is in a correct format.
    """
    girls = open("girlnames2015.txt", "r")
    contents_girls = girls.read()
    girls.close()
    girl_names = contents_girls.split("\n")
    girl_list = []
    for x in girl_names:
        x = x.split()
        name = str(x[1])
        name = girlsclass.gnames(x[0], x[1], x[2])
        girl_list.append(name)
        name = ""
    return girl_list


def play_game(boy, girl, total_questions, total_right, right_guess):
    """
    Description: This function takes the lists from the previous functions, and two other variables and uses them to allow the player to play.
    Inputs: The girl, and boy lists. It also takes two variables at the end which are used to keep track of how many correct guesses and questions the player has received.
    The first time the function runs the last two values are zero.
    Return value: The function returns a list with three values. The first value is the total questions the user has been asked, and the second is how many they have gotten
    correct. The final value is either True or None. If it is True the while loop will continue and will play the game again. If it is None the program will quit.
    Preconditions: The lists need to be filled with class objects, and the final two inputs need to be integers.
    """
    print(
        f"In 2015, was the name {girl.name} (1) or {boy.name} (2) more popular (enter 1 or 2)?"
    )
    # FIXME There is a bug here. I can't fix it. No matter what I do it still will sometimes choose the wrong answer regardless of the math. I have tried moving it all around my code and it still chooses the wrong answer no matter what sometimes. If that looses me points than so be it, but I would love to know what the problem is.
    right_guess = 1 if girl.births > boy.births else 2
    user_guess = int(input())
    total_questions += 1
    if user_guess == right_guess:
        total_right += 1
        print(
            f"Correct. There were {girl.births} girls named {girl.name}, and {boy.births} boys named {boy.name}"
        )
        play_again = input("Would you like to play again (y/n)?\n")
        while play_again != "y" or "n":
            if play_again == "y":
                output = [total_questions, total_right, True]
                return output
            elif play_again == "n":
                output = [total_questions, total_right, None]
                return output
            else:
                print("Please enter yes or no.")
                play_again = input("Would you like to play again (y/n)?\n")
    else:
        print(
            f"Incorrect. There were {girl.births} girls named {girl.name}, and {boy.births} boys named {boy.name}"
        )
        play_again = input("Would you like to play again (y/n)?\n")
        while play_again != "y" or "n":
            if play_again == "y":
                output = [total_questions, total_right, True]
                return output
            elif play_again == "n":
                output = [total_questions, total_right, None]
                return output
            else:
                print("Please enter yes or no.")
                play_again = input("Would you like to play again (y/n)?\n")


# Creating the lists
boy_list = create_boy_list()
girl_list = create_girl_list()

total_questions = 0
total_right = 0
# Setting the play object to allow the while loop to progress.
play = ["blah", "blah", True]

# While loop to keep the game running. Tried to do it inside the function but recursion was not really working for me.
while play[2] == True:
    girl = random.choice(girl_list)
    boy = random.choice(boy_list)
    right_guess = 0
    play = play_game(boy, girl, total_questions, total_right, right_guess)
    total_right = play[1]
    total_questions = play[0]
    continue

# Maths and outputting their percentage.
correct_percentage = total_right / total_questions
print(
    f"You answered {total_right} questions correctly out of {total_questions} for a score of {correct_percentage:.2f}%.\nGoodbye!"
)
print(
    "If you get the stupid bug where it sometimes says the answer is sometimes correct or incorrect even when it shouldn't be please see my fix me note."
)
