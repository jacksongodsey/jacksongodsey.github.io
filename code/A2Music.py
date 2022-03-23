#########################################
# Jackson Godsey
# Assignment a2/Music Assignment
# March 17th, 2022
#
# Description: This program plays a little song
# Inputs: Has no inputs the note's are already in the program.
# Outputs: Plays the song and prints the note as they are played.
# It also switches the instrument at a certain point in the song.
#########################################

# Importing pygame, pygame midi module, and time.
import pygame
import pygame.midi
import time

# Initializing pygame midi module
pygame.midi.init()

def get_output():
    '''
    This function exists to return the default output id of the computer
    it is being ran on. Should make it work on most computers.
    '''
    output = pygame.midi.get_default_output_id()
    return output

# Setting the player object to the output of the above function.
player = pygame.midi.Output(get_output())

# Setting the instrument to a trombone
player.set_instrument(57)

note_tuple = [
    # Note, duration, velocity/volume, Description, instrument
    (69, 0.50, 127, 'A', 57),
    (69, 0.50, 127, 'A', 57),
    (69, 0.50, 127, 'A', 57),
    (65, 0.25, 127, 'F', 57),
    (72, 0.25, 115, 'C', 57),
    (69, 0.50, 127, 'A', 57),
    (65, 0.25, 127, 'F', 57),
    (72, 0.25, 115, 'C', 57),
    (69, 0.75, 127, 'A', 57),
    (64, 0.5, 127, 'E', 57),
    (64, 0.5, 127, 'E', 57),
    (64, 0.5, 127, 'E', 57),
    (65, 0.25, 127, 'F', 57),
    (72, 0.25, 127, 'C', 57),
    (69, 0.5, 127, 'A', 57),
    (65, 0.25, 127, 'F', 57),
    (72, 0.25, 127, 'C', 57),
    (69, 0.75, 127, 'A', 57),
    (0, 3.0, 0, 'Hang on while we change the instrument, and play it again', 57),
    (69, 0.50, 127, 'A', 48),
    (69, 0.50, 127, 'A', 48),
    (69, 0.50, 127, 'A', 48),
    (65, 0.25, 127, 'F', 48),
    (72, 0.25, 115, 'C', 48),
    (69, 0.50, 127, 'A', 48),
    (65, 0.25, 127, 'F', 48),
    (72, 0.25, 115, 'C', 48),
    (69, 0.75, 127, 'A', 48),
    (64, 0.5, 127, 'E', 48),
    (64, 0.5, 127, 'E', 48),
    (64, 0.5, 127, 'E', 48),
    (65, 0.25, 127, 'F', 48),
    (72, 0.25, 127, 'C', 48),
    (69, 0.5, 127, 'A', 48),
    (65, 0.25, 127, 'F', 48),
    (72, 0.25, 127, 'C', 48),
    (69, 0.75, 127, 'A', 48),
    (81, 0.5, 127, 'A something', 48),
    (69, 0.25, 127, 'A', 48),
    (69, 0.25, 127, 'A', 48),
    (81, 0.5, 127, 'A something', 48),
]

def play_note(note_tuple):
    '''
    Description: This function plays a note.
    Inputs: The function takes a tuple of length five as an input.
    Returned value: None it plays a note.
    Preconditions: The tuple must have a length of five.
    '''
    # The four loop takes each note in the tuple and seperates the five values
    # into variables. It prints what the note is, sets the instrument, and
    # plays the note with all it's associated options.
    for i, j, k, l, m in note_tuple:
            print(l)
            player.set_instrument(m)
            player.note_on(i, k)
            time.sleep(j)
            player.note_off(i, k)

# Calling the function.
play_note(note_tuple)

## clean up player and pygame objects
del player
pygame.midi.quit()