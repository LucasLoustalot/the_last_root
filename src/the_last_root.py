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
CONST_POS = (768, 275)

def main():
    pgm = Game((1920,1080),60,"The Last Root","../assets/BG.png")
    pgm.add_object(Player(["../assets/flower/flower_pxl.png"],CONST_POS,0,(400,400),pgm),0)
    pgm.add_object(Upgrade_Button(["../assets/broot.png"],(1750,20),0,(150,150),pgm,button_upgrade_laser, 3), 2)
    pgm.add_object(Upgrade_Button(["../assets/broot.png"],(1580,20),0,(150,150),pgm,button_upgrade_floor, 1), 2)
    pgm.add_object(Upgrade_Button(["../assets/broot.png"],(1410,20),0,(150,150),pgm,button_upgrade_pic, 0), 2)
    pgm.add_object(Upgrade_Button(["../assets/broot.png"],(1240,20),0,(150,150),pgm,button_upgrade_root, 2), 2)
    while (1):
        ant(pgm, CONST_POS)
        last = pygame.time.get_ticks()
        pgm.update()
    return (0)

if __name__ == '__main__':
    main()

