##
# EPITECH PROJECT, 2023
# user_interface.py
# File description:
# User Intarface
##

from game import *
import pygame


class Upgrade_Button(Game_Object):
    def __init__(self, texturepath: list, location: tuple,
                 rotation: int, scale: tuple, game_ref: Game, callback_function,
                 button_text: str):
        super().__init__(location=location, rotation=rotation,
                         scale=scale, game_ref=game_ref)
        self.sprite = Animation(self.location, self.rotation,
                                self.scale, texturepath, 0.1)
        self.sprite.play(loop=False)
        self.callback = callback_function
        self.font = self.game_ref.font
        self.text_str = button_text
        self.textimg = self.font.render(self.text_str, pygame.color.Color(100,100,100),True)
        self.upgrade_level = 0

    def event_tick(self, delta_time: int):
        self.collide_rect = self.sprite.get_rect(self.location, self.rotation)
        frame = self.sprite.get_frame(delta_time)
        self.game_ref.window.blit(frame, self.location)
        self.game_ref.window.blit(self.textimg, self.location)

    def set_upgrade_level(self, level: int):
        self.upgrade_level = level

    def event_click(self, hit_location: tuple):
        print("Truc")
        self.callback(self.game_ref, hit_location)
