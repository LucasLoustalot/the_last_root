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
            self.prix_water = self.game_ref.pic_cost[0]
            self.prix_min = self.game_ref.pic_cost[1]
        if type == 1:
            self.upgrade_level = 1
            self.prix_water = self.game_ref.surface_root_cost[0]
            self.prix_min = self.game_ref.surface_root_cost[1]
        if type == 2:
            self.upgrade_level = 1
            self.prix_water = self.game_ref.g_root_size_cost[0]
            self.prix_min = self.game_ref.g_root_size_cost[1]
        if type == 3:
            self.upgrade_level = 1
            self.prix_water = self.game_ref.pic_cost[0]
            self.prix_min = self.game_ref.pic_cost[1]
        self.text_lvl = str(self.upgrade_level)
        self.text_water = str(self.prix_water)
        self.text_min = str(self.prix_min)
        self.textlvl = self.font.render(self.text_lvl, True, (255, 255, 255))
        self.textwater = self.font.render(
            self.text_water, True, (255, 255, 255))
        self.textmin = self.font.render(self.text_min, True, (255, 255, 255))

    def referesh_text(self):
        self.text_lvl = str(self.upgrade_level)
        self.text_water = str(self.prix_water)
        self.text_min = str(self.prix_min)
        self.textlvl = self.font.render(self.text_lvl, True, (255, 255, 255))
        self.textwater = self.font.render(
            self.text_water, True, (255, 255, 255))
        self.textmin = self.font.render(self.text_min, True, (255, 255, 255))

    def event_tick(self, delta_time: float, fps: float):
        self.collide_rect = self.sprite.get_rect(self.location, self.rotation)
        frame = self.sprite.get_frame(delta_time)
        self.game_ref.window.blit(frame, self.location)
        self.game_ref.window.blit(
            self.textlvl, (self.location[0] + 20, self.location[1] + 100))
        self.game_ref.window.blit(
            self.textwater, (self.location[0] + 120, self.location[1] + 80))
        self.game_ref.window.blit(
            self.textmin, (self.location[0] + 120, self.location[1] + 108))

    def set_upgrade_level(self, level: int):
        self.upgrade_level = level

    def event_clicked(self, hit_location: tuple):
        self.callback(self.game_ref, self)
        self.referesh_text()


def button_upgrade_laser(game: Game, upgrade: Upgrade_Button):
    if game.check_thune(game.g_root_size_cost[0], game.g_root_size_cost[1] - 1) == True:
        
        upgrade.upgrade_level += 1
        """ upgrade.prix_water = game.surface_root_cost[0]
        upgrade.prix_min = game.surface_root_cost[1] """
    else:
        print("Upgrade not available")


def button_upgrade_floor(game: Game, upgrade: Upgrade_Button):

    print("upgrade floor")
    if (game.check_thune(game.surface_root_cost[0], game.surface_root_cost[1]) == True) and (
            game.surface_root_size[0] < game.surface_root_size[1] - 1):
        game.upgrade_surface_root()
        upgrade.prix_water = game.surface_root_cost[0]
        upgrade.prix_min = game.surface_root_cost[1]
        upgrade.upgrade_level += 1
        print("level : " + str(game.surface_root_size[0]))
    else:
        print("Upgrade floor not available")


def button_upgrade_pic(game: Game, upgrade: Upgrade_Button):
    print("upgrade pic")
    if game.check_thune(game.pic_cost[0], game.pic_cost[1]) == True and game.pic_upgrade[0] < game.pic_upgrade[1] - 1:
        game.upgrade_pic()
        upgrade.prix_water = game.pic_cost[0]
        upgrade.prix_min = game.pic_cost[1]
        upgrade.upgrade_level += 1
    else:
        print("Upgrade not available")


def button_upgrade_root(game: Game, upgrade: Upgrade_Button):
    print("upgrade roots")
    if game.check_thune(game.g_root_size_cost[0], game.g_root_size_cost[1]) == True and game.ground_root_size[0] < game.ground_root_size[1] - 1:
        game.upgrade_gnd_root()
        upgrade.prix_water = game.g_root_size_cost[0]
        upgrade.prix_min = game.g_root_size_cost[1]
        upgrade.upgrade_level += 1
    else:
        print("Upgrade not available")
    return
