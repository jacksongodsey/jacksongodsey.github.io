import boysclass
import girlsclass
import random

def create_boy_list():
    boys = open('boynames2015.txt', 'r')
    contents = boys.read()
    boys.close()
    boy_names = contents.split('\n')
    boy_list = []
    for x in boy_names:
        x = x.split()
        name = str(x[1])
        name = boysclass.bnames(x[0], x[1], x[2])
        boy_list.append(name)
        name = ''
    return boy_list
    
def create_girl_list():
    girls = open('girlnames2015.txt', 'r')
    contents_girls = girls.read()
    girls.close()
    girl_names = contents_girls.split('\n')
    girl_list = []
    for x in girl_names:
        x = x.split()
        name = str(x[1])
        name = girlsclass.gnames(x[0], x[1], x[2])
        girl_list.append(name)
        name = ''
    return girl_list

def play_game(boy_list, girl_list):
    random_number = random.randint(0, 999)
    print(f'In 2015, was the name {girl_list[random_number].name} (1) or {boy_list[random_number].name} (2) more popular (enter 1 or 2)?')
    right_guess = 0
    if girl_list[random_number].births > boy_list[random_number].births:
        right_guess = 1
    else:
        right_guess = 2
    user_guess = int(input())
    if user_guess == right_guess:
        print('Correct!')
        play_again = input('Would you like to play again (y/n)?\n')
        if play_again == 'n':
            return None
        elif play_again == 'y':
            play_game(boy_list, girl_list)
    if user_guess != right_guess:
        print(f'Incorrect. There were {girl_list[random_number].births} girls named {girl_list[random_number].name}, and {boy_list[random_number].births} boys named {boy_list[random_number].name}')
        play_again = input('Would you like to play again (y/n)?\n')
        if play_again == 'n':
            return None
        elif play_again == 'y':
            play_game(boy_list, girl_list)

boy_list = create_boy_list()
girl_list = create_girl_list()

play = play_game(boy_list, girl_list)
if play == None:
    print('Goodbye!')




