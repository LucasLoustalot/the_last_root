##
## EPITECH PROJECT, 2023
## heart.py
## File description:
## heart.py
##

from game import *
import pygame

class Heart_Icon(Game_Object):
    def __init__(self, texturepath: list, location: tuple,
                 rotation: int, scale: tuple, game_ref: Game):
        super().__init__(location=location, rotation=rotation,
                         scale=scale, game_ref=game_ref)
        self.sprite = Animation(self.location, self.rotation,
                                self.scale, texturepath, 0.1)
        self.sprite.play(loop=False)
        self.font = pygame.font.Font("../assets/Minecraft.ttf", 48)

    def event_tick(self, delta_time: float, fps: float):
        self.collide_rect = self.sprite.get_rect(self.location, self.rotation)
        frame = self.sprite.get_frame(delta_time)
        self.game_ref.window.blit(frame, self.location)
        self.heart = str(int(self.game_ref.health))
        self.healthtxt = self.font.render(self.heart, True, (255, 100, 100))
        self.game_ref.window.blit(self.healthtxt, (self.location[0] + 120, self.location[1] + 20))
