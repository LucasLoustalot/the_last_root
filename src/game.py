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
        self.layer = 0
        self.collide_rect = None
        self.object_id = 0

    def event_tick(self, delta_time: float, fps: float):
        """Called One Per Frame"""
        return

    def event_clicked(self, hit_location: tuple):
        """Called When Clicked"""
        return

    def event_destroyed(self):
        """Called When the object is destroyed"""
        return


class Animation(pygame.sprite.Sprite):
    def __init__(self, location: tuple, rotation: int, scale: tuple,
                 frames_path: list, delay_ms: float):
        super().__init__()
        self.frames = []
        self.frames_rect = []
        self.delay_ms = delay_ms
        self._index = 0
        self._clock = 0
        self.is_playing = 0
        self.loop = True
        for i in range(0, len(frames_path)):
            self.frames.append(pygame.image.load(
                frames_path[i]).convert_alpha())
            if location[0] == -50:
                self.frames[i] = pygame.transform.flip(
                    self.frames[i], True, False)
            self.frames[i] = pygame.transform.scale(self.frames[i], scale)
            self.frames[i] = pygame.transform.rotate(self.frames[i], rotation)
            self.frames_rect.append(self.frames[i].get_rect(
                topleft=(location[0], location[1])))
        self._max_index = len(self.frames)

    def play(self, loop: bool):
        self.is_playing = True
        self.loop = loop

    def stop(self):
        self.is_playing = False

    def toggle_play(self):
        self.is_playing = not self.is_playing

    def get_rect(self, location: tuple, rotation: int):
        if self._index >= self._max_index:
            self._index = 0
        sprite = self.frames[self._index]
        sprite_rect = self.frames_rect[self._index]
        sprite_rect.center = (sprite_rect.width // 2) + \
            location[0], (sprite_rect.height // 2) + location[1]
        self.frames_rect[self._index] = sprite_rect
        return (self.frames_rect[self._index])

    def get_frame(self, delta_time: float):
        if self.is_playing == False:
            return (self.frames[self._index])
        self._clock += delta_time
        if self._clock >= self.delay_ms:
            self._clock = 0
            if self._index >= self._max_index:
                self._index = 0
                if self.loop == False:
                    self.is_playing = False
            frame = self.frames[self._index]
            self._index += 1
            return (frame)
        else:
            if self._index >= self._max_index:
                self._index = 0
                if self.loop == False:
                    self.is_playing = False
            return (self.frames[self._index])


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
        pygame.font.init()
        pygame.mixer.music.set_volume(0.3)
        pygame.display.set_caption(name)
        self.clock = pygame.time.Clock()
        self.wave = 1
        self.nb_ant = 0
        self.nb = 2.0
        self.window_res = window_res
        self.fps = fps
        self.font = pygame.font.SysFont(pygame.font.get_default_font(), 26)
        self.window = pygame.display.set_mode(
            (self.window_res[0], self.window_res[1]))
        self._background_texture = pygame.image.load(background_path)
        self._background = pygame.transform.scale(
            self._background_texture, self.window_res)
        self.objects = {}
        self.players = []

        self.mineral = 3
        self.water = 6
        self.m_income = 0.05
        self.w_income = 0.1
        # sprites
        self.root_pos = [(735,625),(585,625),(435,625),(285,625),(40,625),(0,625)]
        self.gnd_root_sp = [pygame.image.load(
            "../assets/new_roots/racine_" + str(x + 1) + "_sans_acide.png") for x in range(0, 5)]
        self.sticky_roots_sp = [pygame.image.load(
            "../assets/new_roots/acide_racine_" + str(x+1) + ".png") for x in range(0, 5)]

        # (current/max)
        self.ground_root_size = (0, 4)
        self.surface_root_size = (1, 8)
        self.sticky_roots = (1, 8)
        self.shield_roots = (1, 3)
        self.pic_upgrade = (1, 3)
        # eau,minéraux
        self.g_root_size_cost = (25, 10)
        self.pic_cost = (25, 10)
        self.sticky_root_cost = (10, 30)
        self.shield_roots_cost = (10, 40)
        self.surface_root_cost = (30, 40)

    def add_player(self, player: Game_Object) -> int:
        """Add a player and return a player id"""
        self.players.append(player)
        return (len(self.players) - 1)

    def passive_income(self, fps: float):
        self.water += self.w_income / fps
        self.mineral += self.m_income / fps

    def check_thune(self, water: int, mineral: int) -> bool:
        if self.water >= water and self.mineral >= mineral:
            return (True)
        else:
            return (False)

    def decrase_thune(self, water: int, mineral: int):
        self.water = self.water - water
        self.mineral = self.mineral - mineral

    def upgrade_gnd_root(self):
        mult = 2
        self.ground_root_size = (self.ground_root_size[0] + 1, self.ground_root_size[1])
        self.decrase_thune(self.g_root_size_cost[0], self.g_root_size_cost[1])
        self.g_root_size_cost = (self.g_root_size_cost[0] * mult, self.g_root_size_cost[1] * mult)

    def upgrade_sticky_root(self):
        mult = 2
        self.sticky_roots = (self.g_root_size_cost[0] + 1, self.g_root_size_cost[1]) 
        self.decrase_thune(self.g_root_size_cost[0], self.g_root_size_cost[1])
        self.sticky_root_cost = (self.sticky_root_cost[0] * mult, self.sticky_root_cost[1] * mult)

    def upgrade_surface_root(self):
        mult = 2
        self.surface_root_size = (self.g_root_size_cost[0] + 1, self.g_root_size_cost[1])
        self.decrase_thune(self.g_root_size_cost[0], self.g_root_size_cost[1])
        self.surface_root_cost = (self.surface_root_cost[0] * mult, self.surface_root_cost[1] * mult)

    def upgrade_pic(self):
        mult = 2
        self.pic_upgrade = (self.pic_upgrade[0] + 1, self.pic_upgrade[1])
        self.decrase_thune(self.pic_upgrade[0], self.pic_upgrade[1])
        self.pic_cost = (self.pic_cost[0] * mult, self.pic_cost[1] * mult)

    def refresh_upgrades(self):
        srf_root_path = "../assets/racine_surface/racine"
        for i in range(1, self.ground_root_size[0]):
            pth = srf_root_path + \
                str(i) + "_" + \
                "avec" if self.sticky_roots[0] >= i else "sans" + "acide.png"

    def remove_player(self, player_id):
        self.players.pop(player_id)

    def add_object(self, Object: Game_Object, layer: int) -> int:
        """Add an object and return an object id"""
        obj = Object
        obj.layer = layer
        if str(layer) not in self.objects:
            self.objects[str(layer)] = {}
        obj.object_id = len(self.objects[str(layer)])
        self.objects[str(layer)][str(obj.object_id)] = obj
        return (obj.object_id)

    def remove_object_by_id(self, layer: int, Object_id: int):
        self.objects[str(layer)][str(Object_id)].event_destroyed()
        self.objects[str(layer)][str(Object_id)] = None

    def __garbage_collector(self):
        """Private Method
        - Internal use only"""
        for layer, layer_obj in self.objects.items():
            for key in layer_obj:
                if layer_obj[key] == None:
                    del layer_obj[key]
                    self.__garbage_collector()
                    return

    def __update_event(self):
        """Private Method
        - Internal use only"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for layer, layer_obj in self.objects.items():
                    for key in layer_obj:
                        if layer_obj[key].collide_rect.collidepoint(event.pos):
                            layer_obj[key].event_clicked(event.pos)
                            return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

    def draw_upgrades(self):
        self.window.blit(self.gnd_root_sp[self.ground_root_size[0]],self.root_pos[self.ground_root_size[0]])
        #self.window.blit(self.sticky_roots_sp[self.sticky_roots[0] - 1],self.root_pos[self.ground_root_size[0] - 1])
        return

    def update(self):
        """Update the window and the game by refreshing every game object added"""
        self.__update_event()
        self.window.blit(self._background, (0, 0))
        self.__garbage_collector()
        tick = self.clock.tick(60)
        fps = 1000.0 / tick
        self.passive_income(fps)
        # print("Eau : " + str(self.water) + " Minerais : " + str(self.mineral))
        for layer, layer_obj in self.objects.items():
            for key in layer_obj:
                layer_obj[key].event_tick(tick / 1000, fps)
        self.draw_upgrades() #993 660
        pygame.display.flip()
        return
