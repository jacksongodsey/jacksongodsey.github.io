import random
random.seed()

def playgame(boy_name_list, girl_name_list):
    

f = open('girlnames2015.txt', 'r')
q = open('boynames2015.txt', 'r')
girl_name_list = []
boy_name_list = []
for x in f:
    x = x.split()
    girl_name_list.append(tuple([x[0], x[1], x[2]]))
for z in q:
    z = z.split()
    boy_name_list.append(tuple([z[0], z[1], z[2]]))
