import pygame
import pygame.midi
import time


pygame.midi.init()
player = pygame.midi.Output(5)

player.set_instrument(41)


def music_function(note_tuple):
    for i, j, k in note_tuple:
        player.note_on(i, k)
        time.sleep(j)
        player.note_off(i, k)


note_tuple = [
    (69, 0.5, 127),
    (66, 0.25, 127),
    (67, 0.25, 127),
    (69, 0.5, 127),
    (66, 0.25, 127),
    (67, 0.25, 127),
    (69, 0.25, 127),
    (57, 0.25, 127),
    (59, 0.25, 127),
    (61, 0.25, 127),
    (62, 0.25, 127),
    (64, 0.25, 127),
    (66, 0.25, 127),
    (67, 0.25, 127),
    (66, 0.5, 127),
    (62, 0.25, 127),
    (64, 0.25, 127),
    (66, 0.5, 127),
]

music_function(note_tuple)

## clean up player and pygame objects
del player
pygame.midi.quit()
