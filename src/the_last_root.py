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
from ressource_item import *
from heart import *
from vague import *
CONST_POS = (768, 275)

def main():
    [pygame.image.load(
            "../assets/new_roots/racine_" + str(x + 1) + "_sans_acide.png") for x in range(0, 5)]

    pgm = Game((1920,1080),60,"The Last Root","../assets/BG.png")
    pgm.add_object(Player(["../assets/animation_plante/f" + str(x) + ".png" for x in range(1,12)],CONST_POS,0,(400,400),pgm),0)
    pgm.add_object(Upgrade_Button(["../assets/panneaux_test.png"],(1750,20),0,(150,150),pgm,button_upgrade_laser, 3), 2)
    pgm.add_object(Upgrade_Button(["../assets/panneaux_test.png"],(1580,20),0,(150,150),pgm,button_upgrade_floor, 1), 2)
    pgm.add_object(Upgrade_Button(["../assets/panneaux_test.png"],(1410,20),0,(150,150),pgm,button_upgrade_pic, 0), 2)
    pgm.add_object(Upgrade_Button(["../assets/button_root.png"],(1240,20),0,(150,150),pgm,button_upgrade_root, 2), 2)
    pgm.add_object(Ressource_Button(["../assets/eau.png"], (35, 115), 0, (53,83), pgm, 0), 2)
    pgm.add_object(Ressource_Button(["../assets/mineraux.png"], (20, 20), 0, (75,75), pgm, 1), 2)
    pgm.add_object(Heart_Icon(["../assets/heart.png"], (275, 20), 0, (122, 81), pgm), 2)
    pgm.add_object(Wave_Count((885, 30), 0, (150, 150), pgm), 2)
    while (1):
        ant(pgm, CONST_POS)
        pgm.update()
    return (0)

if __name__ == '__main__':
    main()
