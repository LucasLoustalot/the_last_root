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
                 rotation: int, scale: tuple, game_ref: Game, callback_function, type: int):
        super().__init__(location=location, rotation=rotation,
                         scale=scale, game_ref=game_ref)
        self.sprite = Animation(self.location, self.rotation,
                                self.scale, texturepath, 0.1)
        self.sprite.play(loop=False)
        self.callback = callback_function
        self.font = pygame.font.Font("../assets/Minecraft.ttf", 28)
        if type == 0:
            self.upgrade_level = 0
            self.prix_water = 8
            self.prix_min = 3
            self.text_lvl = str(self.upgrade_level)
            self.textlvl = self.font.render(self.text_lvl, True, (255, 255, 255))
        if type == 1:
            self.upgrade_level = 1
            self.prix_water = 5
            self.prix_min = 2
            self.text_lvl = str(self.upgrade_level)
            self.textlvl = self.font.render(self.text_lvl, True, (255, 255, 255))
        if type == 2:
            self.upgrade_level = 1
            self.prix_water = 6
            self.prix_min = 4
            self.text_lvl = str(self.upgrade_level)
            self.textlvl = self.font.render(self.text_lvl, True, (255, 255, 255))
        if type == 3:
            self.upgrade_level = 1
            self.prix_water = 8
            self.prix_min = 5
            self.text_lvl = str(self.upgrade_level)
            self.textlvl = self.font.render(self.text_lvl, True, (255, 255, 255))

    def event_tick(self, delta_time: float, fps: float):
        self.collide_rect = self.sprite.get_rect(self.location, self.rotation)
        frame = self.sprite.get_frame(delta_time)
        self.game_ref.window.blit(frame, self.location)
        self.game_ref.window.blit(self.textlvl, (self.location[0] + 20, self.location[1] + 100))

    def set_upgrade_level(self, level: int):
        self.upgrade_level = level

    def event_clicked(self, hit_location: tuple):
        self.callback(self.game_ref, self)


def button_upgrade_laser(game: Game, upgrade: Upgrade_Button):
    if game.check_thune(game.g_root_size_cost[0], game.g_root_size_cost[1]) == True:
        game.upgrade_gnd_root()
    else :
        print("Not enough money")

def button_upgrade_floor(game: Game, upgrade: Upgrade_Button):
    print("upgrade floor")
    if game.check_thune(game.surface_root_cost[0], game.surface_root_cost[1]) == True:
        game.upgrade_gnd_root()
    else :
        print("Not enough money")

def button_upgrade_pic(game: Game, upgrade: Upgrade_Button):
    print("upgrade pic")
    if game.check_thune(game.pic_cost[0], game.pic_cost[1]) == True:
        game.upgrade_gnd_root()
    else :
        print("Not enough money")

def button_upgrade_root(game: Game, upgrade: Upgrade_Button):
    print("upgrade roots")
    if game.check_thune(game.g_root_size_cost[0], game.g_root_size_cost[1]) == True:
        game.upgrade_gnd_root()
    else :
        print("Not enough money")
    return
