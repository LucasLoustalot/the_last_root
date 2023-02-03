##
## EPITECH PROJECT, 2023
## the_last_root.py
## File description:
## Game main file
##

import pygame
from game import *
from player import *

def main():
    pgm = Game((1600,800),60,"The Last Root","photobg.jpg")
    pgm.add_object(Player("photobg.jpg",(0,0),0,(100,100),pgm),1)
    while (1):
        pgm.update()
    return (0)

if __name__ == '__main__':
    main()

