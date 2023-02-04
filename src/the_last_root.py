##
## EPITECH PROJECT, 2023
## the_last_root.py
## File description:
## Game main file
##

import pygame
from game import *
from player import *
from ant import *
from user_interface import *
CONST_POS = (800, 400)

def main():
    pgm = Game((1600,800),60,"The Last Root","../assets/photobg.jpg")
    pgm.add_object(Player(["../assets/flower1.png","../assets/photobg.jpg"],CONST_POS,0,(400,400),pgm),0)
    pgm.add_object(Upgrade_Button(["../assets/broot.png"],(1440,5),0,(150,150),pgm,button_upgrade_laser), 2)
    pgm.add_object(Upgrade_Button(["../assets/broot.png"],(1270,5),0,(150,150),pgm,button_upgrade_floor), 2)
    pgm.add_object(Upgrade_Button(["../assets/broot.png"],(1100,5),0,(150,150),pgm,button_upgrade_pic), 2)
    pgm.add_object(Upgrade_Button(["../assets/broot.png"],(930, 5),0,(150,150),pgm,button_upgrade_root), 2)

    while (1):
        ant(pgm, CONST_POS)
        last = pygame.time.get_ticks()
        pgm.update()
    return (0)

if __name__ == '__main__':
    main()

