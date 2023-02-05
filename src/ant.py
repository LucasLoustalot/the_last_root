##
# EPITECH PROJECT, 2023
# ant.py
# File description:
# ant.py
##

from game import *
from player import *
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
        self.health = 100
        self.damage = 3
        self.hit = 0
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
        self.game_ref.remove_object_by_id(self.layer, self.object_id)
        self.game_ref.nb_ant -= 1
        return

def damage(ant: Ant, fps: float):
    if (ant.hit == 1 and ant.game_ref.health > 0):
        ant.game_ref.health -= 3 / fps
    if (ant.game_ref.health <= 0):
        ant.game_ref.clear_objects()

def ant(game: Game, pos: tuple):
    global clock_time, delay, nb_spawn
    if int(game.nb_ant) == 0:
        game.nb = game.nb + 0.25 + round(random.uniform(0.1, 0.4), 1)
        game.nb_ant = int(game.nb)
        game.wave += 1
        clock_time = 0
        nb_spawn = 0
        dealy = 0
    if nb_spawn != int(game.nb):
        clock_time += game.clock.tick(60)
    if clock_time >= delay :
        random1 = random.choice([-50, 1900])
        nb_spawn += 10
        game.add_object(Ant(["../assets/ant.png"], (random1, 600),
            angle_player(pos, (random1, 600)), (70, 70), game, pos), 1)
        delay = random.randint(300, 900)
        clock_time = 0

def angle_player(pos, pos2):
    x1, y1 = pos
    x2, y2 = pos2
    x_diff = x2 - x1
    y_diff = y2 - y1
    return math.degrees(math.atan2(y_diff, x_diff))
