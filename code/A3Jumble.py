#########################################
# Jackson Godsey
# Assignment 3
# 03/31/2022
#
# Description: This program takes user input of a jumbled word then outputs -
# any word that can be spelt with the jumbled word. It also outputs three -
# words that have already been hardcoded into the program.
# Inputs: A words.txt file containing thousands of words, as well as a user inputted -
# jumbled word.
# Output: The program outputs multiple items. If the word that the user inputs -
# can be successfuly spelled with other words that it will output those. If not -
# the program outputs the phrase "no word found". After that is completted the program -
# outputs three hardcoded words, and what they can be unscrambled too if at all possible.
# I got help figuring out the assignment from Mika or Winter-Stark in the UAA Computer Science and Engineering discord.
# I was having a hard time with figuring out the functions and she helped point in the right direction.
#########################################
words = open('words.txt', 'r')
contents = words.read()
words.close()

contents.strip()
word_list = contents.split()

def build_dict(word_list):
    '''
    Description: This function builds a dictionary of any words that can be spelled the same way.
    Inputs: This function takes a word list as input that will be used to build the dictionary.
    Returned value: The function returns a dictionary that contains all the words in the list
    that can be spelled with identical characters. For example in the case of the words:
    bat and tab they are set as values to the sorted word abt that is a key in the dictionary.
    Preconditions: The word list must actually be a list, and contain words.
    '''
    dictionary = {}
    for word in word_list:
        temp = ''.join(sorted(word))
        if temp in dictionary:
            dictionary[temp].append(word)
        else:
            dictionary[temp] = [word]
    return dictionary

def unscrambled(jumble, sorted_dict):
    '''
    Description: This function turns the user inputted scrambled word, and the dictionary
    sorted by the previous function and simply sorts the jumbled word alphabettically.
    It then turns that word into a string, and compares that to the dictionary. It then returns
    the values associated with that key. If there isn't a match it returns none.
    Inputs: the user inputted scrambled word, and the sorted dictionary
    Returned value: All the values asscociated with the key given by the sorted jumbled word.
    If there is not a match it returns the None value.
    Preconditions: None in particular. Just the jumbled word and the dictionary from
    the previous function.
    '''
    temp = ''.join(sorted(jumble))
    return sorted_dict.get(temp)

scrambled = input("Please enter a jumble to solve: ")
sorted_dict = build_dict(word_list)
output = unscrambled(scrambled, sorted_dict)

if output == None:
    print(f'No word found {scrambled}')
else:
    print(f'{scrambled} unscrambles to: {output}')

hardcoded_list = ['asewes', 'enost', 'aaabcs']

for i in range(len(hardcoded_list)):
    scrambled = hardcoded_list[i]
    output = unscrambled(scrambled, sorted_dict)
    if output == None:
        print(f'No word found {scrambled}')
    else:
        print(f'{scrambled} unscrambles to: {output}')
