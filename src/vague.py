##
## EPITECH PROJECT, 2023
## wave.py
## File description:
## wave.py
##

from game import *
from player import *
import pygame

class Wave_Count(Game_Object):
    def __init__(self, location: tuple,
                 rotation: int, scale: tuple, game_ref: Game):
        super().__init__(location=location, rotation=rotation,
                         scale=scale, game_ref=game_ref)
        self.font = pygame.font.Font("../assets/Minecraft.ttf", 48)

    def event_tick(self, delta_time: float, fps: float):
        self.vague = "Wave : " + str(int(self.game_ref.wave))
        self.vaguetxt = self.font.render(self.vague, True, (0, 154, 23))
        self.game_ref.window.blit(self.vaguetxt, (self.location))
