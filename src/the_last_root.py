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
    pgm.add_object(Upgrade_Button(["../assets/playbtnplaceholder.png"],(200,200),0,(500,100),pgm,""),1)
    ant(pgm, CONST_POS)

    while (1):
        pgm.update()
        if pgm.nb_ant == 0:
            pgm.wave += 1
            ant(pgm, CONST_POS)
    return (0)

if __name__ == '__main__':
    main()

