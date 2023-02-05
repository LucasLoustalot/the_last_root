##
# EPITECH PROJECT, 2023
# ant.py
# File description:
# ant.py
##

from game import *
from player import *
from user_interface import Effect
import pygame
import random
import math
import time
antl = []
clock_time = 0
delay = 0
nb_spawn = 0

class Ant(Game_Object):
    """Ant Specific Class"""

    def __init__(self, texturespath: list, location: tuple,
                 rotation: int, scale: tuple, game_ref: Game, target_loc: tuple):
        super().__init__(location=location, rotation=0,
                         scale=scale, game_ref=game_ref)
        self.flip = True if rotation < 120 else False
        self.health = 10 + 0.1 * game_ref.wave + (random.randint(0,4) / 4)
        self.damage = 3 + random.randint(0,2) + 0.2 * game_ref.wave
        self.hit = 0
        self.is_boss = False
        self.boss_rd = random.randint(0,25)
        if self.boss_rd == 25:
            self.is_boss = True
            self.health *= 2
            self.damage *= 1.5
            self.scale = (self.scale[0] + 20, self.scale[1] + 20)
            self.location = (self.location[0], self.location[1] - 20)
        self.sprite = Animation(self.location, self.rotation,
                                self.scale, texturespath, 0.1)
        self.sprite.play(loop=False)
        self.target_location = target_loc
        self.speed = 100

    def event_tick(self, delta_time: float, fps: float):
        err = 50
        correct = 187
        sp = self.speed / fps
        if self.flip == True:
            sp = sp * -1
        if not (self.location[0] <= self.target_location[0] + err + correct and
                self.location[0] >= self.target_location[0] - err + correct):
            self.location = (
                self.location[0] + math.cos(self.rotation) * sp, self.location[1])
        else:
            self.hit = 1
        self.collide_rect = self.sprite.get_rect(self.location, self.rotation)
        frame = self.sprite.get_frame(delta_time)
        self.game_ref.window.blit(frame, self.location)
        damage(self, fps)

    def event_clicked(self, hit_pos: tuple):
        if self.game_ref.check_thune(self.game_ref.solar_power_cost[0] / self.game_ref.solar_power[0], self.game_ref.solar_power_cost[0] / self.game_ref.solar_power[0]) == True:
            self.game_ref.water -= self.game_ref.solar_power_cost[0] / self.game_ref.solar_power[0]
            self.game_ref.mineral -= self.game_ref.solar_power_cost[1] / self.game_ref.solar_power[0]
            self.game_ref.remove_object_by_id(1, self.object_id)
            self.game_ref.nb_ant -= 1
            self.game_ref.add_object(Effect(["../assets/explo/" + str(x) + ".png" for x in range(0, 5)],
            self.location,0,(self.scale[0] * 1.2, self.scale[1] * 1.2),self.game_ref),0)
        return

    def receive_damage(self, damage: int):
        self.health = self.health - damage
        if self.health <= 0 :
            self.game_ref.remove_object_by_id(self.layer, self.object_id)
            self.game_ref.nb_ant -= 1

def check_ant(ant: Ant):
    if int(ant.health) == 0:
        ant.game_ref.remove_object_by_id(1, ant.object_id)
        ant.game_ref.nb_ant -= 1

def damage(ant: Ant, fps: float):
    if (ant.hit == 1 and ant.game_ref.health > 0):
        ant.game_ref.health -= ant.damage / fps
    if (ant.game_ref.health <= 0):
        ant.game_ref.clear_objects()
        ant.game_ref.nb_ant -= 1
        print("dead")

def ant(game: Game, pos: tuple):
    global clock_time, delay, nb_spawn
    if int(game.nb_ant) == 0:
        game.nb = game.nb + 0.25 + round(random.uniform(0.1, 0.4), 1)
        game.nb_ant = int(game.nb)
        game.wave += 1
        clock_time = 0
        nb_spawn = 0
    if nb_spawn != int(game.nb):
        clock_time += game.clock.tick(60)
    if clock_time >= delay :
        random1 = random.choice([-50, 1900])
        nb_spawn += 10
        game.add_object(Ant(["../assets/cafard.png"], (random1, 600),
            angle_player(pos, (random1, 600)), (70, 70), game, pos), 1)
        delay = random.randint(300, 900)
        clock_time = 0

def angle_player(pos, pos2):
    x1, y1 = pos
    x2, y2 = pos2
    x_diff = x2 - x1
    y_diff = y2 - y1
    return math.degrees(math.atan2(y_diff, x_diff))
