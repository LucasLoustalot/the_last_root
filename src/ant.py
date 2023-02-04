##
## EPITECH PROJECT, 2023
## ant.py
## File description:
## ant.py
##

from game import *
import pygame
import random
import math
antl = []

class Ant(Game_Object):
    """Ant Specific Class"""

    def __init__(self, texturespath: list, location: tuple,
                 rotation: int, scale: tuple, game_ref: Game):
        super().__init__(location=location, rotation=rotation,
                         scale=scale, game_ref=game_ref)
        self.health = 100
        self.sprite = Animation(self.location, self.rotation,
        self.scale, texturespath, 0.1)
        self.sprite.play(loop=False)

    def event_tick(self, delta_time: int):

        self.collide_rect = self.sprite.get_rect(self.location, self.rotation)
        frame = self.sprite.get_frame(delta_time)
        self.game_ref.window.blit(frame, self.location)

    def event_clicked(self, hit_pos: tuple):
        return

def ant(game: Game, pos: tuple):
    j = 1
    for i in range(0, 5):
        random1 = random.choice([0, 1500])
        random2 = random.randint(0, 800)
        antl.append(Ant(["../assets/ant.png","../assets/ant.png"],
        (random1, random2), angle_player(pos, (random1, random2)), (150, 150), game))
    for i in range(0, 5):
        game.add_object(antl[i], 1)

def angle_player(pos, pos2):
    x1, y1 = pos
    x2, y2 = pos2
    x_diff = x2 - x1
    y_diff = y2 - y1git
    return math.degrees(math.atan2(y_diff, x_diff))
