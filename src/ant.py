##
## EPITECH PROJECT, 2023
## ant.py
## File description:
## ant.py
##

from game import *
import pygame

class Ant(Game_Object):
    """Ant Specific Class"""

    def __init__(self, texturespath: list, location: tuple,
                 rotation: int, scale: tuple, game_ref: Game):
        super().__init__(location=location, rotation=rotation,
                         scale=scale, game_ref=game_ref)
        self.health = 100
        self.sprite = Animation(self.location, self.rotation,
        self.scale, texturespath, 0.1)
        self.sprite.play()

    def event_tick(self, delta_time: int):
        frame = self.sprite.get_frame(delta_time)
        self.collide_rect = frame.get_rect()
        self.game_ref.window.blit(frame, self.location)

    def event_clicked(self):
        return

def ant(game: Game):
    j = 1
    antl = []
    for i in range(0, j * 5):
        antl.append(Ant(["../assets/ant.png","../assets/ant.png"],
        (20 + ((i + j) * 200), 20),0, (200, 200), game))
    for i in range(0, j * 5):
        game.add_object(antl[i], 1)

