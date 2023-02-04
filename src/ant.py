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


class Ant(Game_Object):
    """Ant Specific Class"""

    def __init__(self, texturespath: list, location: tuple,
                 rotation: int, scale: tuple, game_ref: Game, target_loc: tuple):
        super().__init__(location=location, rotation=rotation,
                         scale=scale, game_ref=game_ref)
        self.health = 100
        self.sprite = Animation(self.location, self.rotation,
                                self.scale, texturespath, 0.1)
        self.sprite.play(loop=False)
        self.target_location = target_loc

    def event_tick(self, delta_time: int):

        err = 0.5
        if (self.location[0] <= self.target_location[0] + 0.5 and 
        self.location[0] >= self.target_location[0]) :
            return

    '''if ((pos.x <= tgpos.x + threshold & & pos.x >=
         tgpos.x - threshold) & & (pos.y <= tgpos.y + threshold
                                   & & pos.y >= tgpos.y - threshold)) {
        if (ac -> is_active == -1)
        return
        remove_aircraft(ac, rd)
        return
    }
    sfSprite_setPosition(ac -> ac_sprite,
                         (sfVector2f){pos.x + (cos(angle) * sp),
                                      pos.y + (sin(angle) * sp)})
    sfRectangleShape_setPosition(ac -> col_rect, (sfVector2f)
                                 {pos.x + (cos(angle) * sp),
                                  pos.y + (sin(angle) * sp)})
    '''
    self.collide_rect = self.sprite.get_rect(self.location, self.rotation)
    frame = self.sprite.get_frame(delta_time)
    self.game_ref.window.blit(frame, self.location)

    def event_clicked(self, hit_pos: tuple):
        self.game_ref.remove_object_by_id(1, self.object_id)
        self.game_ref.nb_ant -= 1
        return


def ant(game: Game, pos: tuple):
    game.nb = game.nb + 0.25 + round(random.uniform(0.1, 0.4), 1)
    game.nb_ant = int(game.nb)
    for i in range(0, game.nb_ant):
        random1 = random.choice([-50, 1500])
        game.add_object(Ant(["../assets/ant.png", "../assets/ant.png"], (random1, 600),
                            angle_player(pos, (random1, 600)), (70, 70), game, pos), 1)


def angle_player(pos, pos2):
    x1, y1 = pos
    x2, y2 = pos2
    x_diff = x2 - x1
    y_diff = y2 - y1
    return math.degrees(math.atan2(y_diff, x_diff))
