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

    def __init__(self, texturepath: str, location: tuple,
                 rotation: int, scale: tuple, game_ref: Game):
        super().__init__(location=location, rotation=rotation,
                         scale=scale, game_ref=game_ref)
        self.health = 100
        self.upgrades = []
        self.texture = pygame.image.load(texturepath).convert_alpha()
        self.sprite = pygame.transform.scale(self.texture, self.scale)
        self.texture_rect = self.texture.get_rect()

    def event_tick(self):
        self.game_ref.window.blit(self.sprite, self.location)
