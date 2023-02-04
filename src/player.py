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

    def __init__(self, texturespath: list, location: tuple,
                 rotation: int, scale: tuple, game_ref: Game):
        super().__init__(location=location, rotation=rotation,
                         scale=scale, game_ref=game_ref)
        self.health = 100
        self.upgrades = []
        self.sprite = Animation(self.location, self.rotation,
                                self.scale, texturespath, 0.1)
        self.sprite.play(loop=False)

    def event_tick(self, delta_time: int):
        frame = self.sprite.get_frame(delta_time)
        self.collide_rect = frame.get_rect(topleft=(self.location[0], self.location[1]))
        self.game_ref.window.blit(frame, self.location)

    def event_clicked(self, hit_location: tuple):
        return