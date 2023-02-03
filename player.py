##
# EPITECH PROJECT, 2023
# player.py
# File description:
# Player File
##

from game import *
import pygame


class Player(Game_Object):
    """Player Specific Class"""

    def __init__(self, texturepath: str):
        super().__init__()
        self.health = 100
        self.upgrades = []
        self.texture = pygame.image.load(texturepath).convert_alpha()
        self.sprite = pygame.transform.scale(self.image, self.scale)
        self.texture_rect = self.image.get_rect()
