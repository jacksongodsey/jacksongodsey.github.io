#########################
#      Luka Richardson
#      Assignment A2, music
#      Date completed: March 17
#      Description: The purpose of this code is to play a song
#
#
#
#########################

import pygame.midi
import time
pygame.midi.init()
player = pygame.midi.Output(5)
player.set_instrument(0)
note_list = (
    (56, 0.5, 127),
    (56, 0.5, 127),
    (54, 1.0, 127),
    (54, 1.0, 127),
    (54, 1.0, 127),
    (39, 1.0, 127),
    (39, 1.0, 127),
    (39, 1.0, 127),
    (56, 0.5, 127),
    (54, 1.0, 127),
    (54, 1.0, 127),
)
def play_music(note_list):
    for x, y, z in note_list:
        player.note_on(x, z)
        time.sleep(y)
        player.note_off(x,z)

play_music(note_list)

del player
pygame.midi.quit()