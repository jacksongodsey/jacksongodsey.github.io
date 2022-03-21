# use this file as a starting point for your MidiMusic program

## can't send to shell -- must type it into the interpreter window
#pip install pygame

# for python version 3.8, must install a development version of pygame:
#pip install pygame==2.0.0.dev10
# https://stackoverflow.com/questions/60658069/error-when-installing-pygame-on-mac-error-command-gcc-failed-with-exit-statu

# for python version 3.9, must install this version:
#pip install pygame==2.0.0.dev14

# to check the version installed, type:
#pip show pygame

# https://www.pygame.org/docs/ref/midi.html
import pygame
import pygame.midi
import time # for putting the program to 'sleep'


## initialize midi player
pygame.midi.init()
player = pygame.midi.Output(0)

##
# for the list of MIDI instruments:
#    https://soundprogramming.net/file-formats/general-midi-instrument-list/
# be sure to delete the player object before changing instruments
player.set_instrument(1)

## play 4 notes; modify the following code by putting it into a function
note = (60,0.5,127) # use a tuple to specify (note_tone, duration, velocity)
player.note_on(note[0], note[2])
time.sleep(note[1])
player.note_off(note[0], note[2])

player.note_on(note[0], note[2])
time.sleep(note[1])
player.note_off(note[0], note[2])

note = (67,1.0,127)
player.note_on(note[0], note[2])
time.sleep(note[1])
player.note_off(note[0], note[2])

player.note_on(note[0], note[2])
time.sleep(note[1])
player.note_off(note[0], note[2])


## list of tuples hint
note_list = [
    (60,1.0,127),
    (60,1.0,127),
    (67,1.0,127),
    (67,1.0,127),
    (70,2.0,127)
    ]
for note in note_list:
    print(note)

## example of playing a chord for bonus problem
# again, be sure to put this code into a function with appropriate parameters
player.note_on(60, 127)
player.note_on(64, 127)
player.note_on(67, 127)
player.note_on(72, 127)
time.sleep(2)
player.note_off(60, 127)
player.note_off(64, 127)
player.note_off(67, 127)
player.note_off(72, 127)

offset = 4
player.note_on(60+offset, 127)
player.note_on(64+offset, 127)
player.note_on(67+offset, 127)
player.note_on(72+offset, 127)
time.sleep(2)
player.note_off(60+offset, 127)
player.note_off(64+offset, 127)
player.note_off(67+offset, 127)
player.note_off(72+offset, 127)

## optional: could improve readability by using a dictionary...
note_lookup = {'C':60, 'C#':61, 'D':62}
note = (note_lookup['C#']-12, 1.0, 127) # 12 half-steps is an octive
print(note)



## clean up player and pygame objects
del player
pygame.midi.quit()
