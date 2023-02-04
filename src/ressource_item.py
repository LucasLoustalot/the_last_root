##
## EPITECH PROJECT, 2023
## ressource_item.py
## File description:
## ressource_item.py
##

from game import *
import pygame

class Ressource_Button(Game_Object):
    def __init__(self, texturepath: list, location: tuple,
                 rotation: int, scale: tuple, game_ref: Game, type: int):
        super().__init__(location=location, rotation=rotation,
                         scale=scale, game_ref=game_ref)
        self.sprite = Animation(self.location, self.rotation,
                                self.scale, texturepath, 0.1)
        self.sprite.play(loop=False)
        self.font = pygame.font.Font("../assets/Minecraft.ttf", 48)
        self.type = type

    def event_tick(self, delta_time: float, fps: float):
        self.collide_rect = self.sprite.get_rect(self.location, self.rotation)
        frame = self.sprite.get_frame(delta_time)
        self.game_ref.window.blit(frame, self.location)
        if self.type == 0:
            self.water = str(int(self.game_ref.water))
            self.textwater = self.font.render(self.water, True, (255, 255, 255))
            self.textmin = None
        if self.type == 1:
            self.min = str(int(self.game_ref.mineral))
            self.textmin = self.font.render(self.min, True, (255, 255, 255))
            self.textwater = None
        if self.textwater != None:
            self.game_ref.window.blit(self.textwater, (self.location[0] + 90, self.location[1] + 20))
        if self.textmin != None:
            self.game_ref.window.blit(self.textmin, (self.location[0] + 90, self.location[1] + 20))
