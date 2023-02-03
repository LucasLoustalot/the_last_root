##
# EPITECH PROJECT, 2023
# game.py
# File description:
# Game Engine
##

import pygame

class Game_Object(pygame.sprite.Sprite):
    """Master game object, parent of all other object classes.
    - Do not add gameplay specific functions here."""

    def __init__(self, location: tuple, rotation: int, scale: tuple, game_ref):
        super().__init__()
        self.game_ref = game_ref
        self.location = location
        self.rotation = rotation
        self.scale = scale

    def event_tick(self):
        """Called One Per Frame"""
        return

    def event_clicked(self):
        """Called When Clicked"""
        return


class Game():
    """Master class of the game, it contains:
    - the list of all active object
    - initialised classes from pygame (mixer, window, font, clock)
    - methods to add or remove objects

    This class needs to be updated in a loop by calling the update() function.
    """

    def __init__(self, window_res: tuple, fps: int, name: str, background_path: str):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.set_volume(0.3)
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.window_res = window_res
        self.fps = fps
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 26)
        self.window = pygame.display.set_mode(
            (self.window_res[0], self.window_res[1]))
        self._background_texture = pygame.image.load(background_path)
        self._background = pygame.transform.scale(
            self._background_texture, self.window_res)
        self.objects = {}

    def add_object(self, Object: Game_Object, layer: int):
        if str(layer) not in self.objects:
            self.objects[str(layer)] = []
        self.objects[str(layer)].append(Object)

    def remove_object(self, Object: Game_Object, layer: int):
        self.objects[str(layer)].remove(Object)

    def __update_event(self):
        """Private Method
        - Internal use only"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def update(self):
        """Update the window and the game by refreshing every game object added"""
        self.__update_event()
        self.window.blit(self._background, (0,0))
        for layer, layer_obj in self.objects.items():
            for obj in layer_obj:
                obj.event_tick()
        pygame.display.flip()
        return
