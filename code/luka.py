#########################
#      Luka Richardson
#      Assignment A2, music
#      Date completed: March 17
#      Description: The purpose of this code is to play a song
#
#
#
#########################

user_input = input()
entries = user_input.split(',')
country_pop = {}

for pair in entries:
    split_pair = pair.split(':')
    country_pop[split_pair[0]] = split_pair[1]
    # country_pop is a dictionary, Ex: { 'Germany':'82790000', 'France':'67190000' }
    for i in country_pop.keys():
        country = i
    for i in country_pop.values():
        pop = i
    print(country, 'has', pop, 'people.')