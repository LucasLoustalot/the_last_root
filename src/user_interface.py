##
# EPITECH PROJECT, 2023
# user_interface.py
# File description:
# User Intarface
##

from game import *
import pygame


class Upgrade_Button(Game_Object):
    def __init__(self, texturepath: str, location: tuple,
                 rotation: int, scale: tuple, game_ref: Game, callback_function, ):
        super().__init__(location=location, rotation=rotation,
                         scale=scale, game_ref=game_ref)
        self.sprite = pygame.image.load(texturepath).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, self.scale)
        self.sprite = pygame.transform.rotate(self.sprite, self.rotation)
        self.callback = callback_function
        self.font = self.game_ref.font
        self.
        self.upgrade_level = 0

    def set_upgrade_level(self, level: int):
        self.upgrade_level = level

    def event_hovered(self):
        # This function is not called
        return

    def event_click(self, hit_location: tuple):
        self.callback(self.game_ref, hit_location)
