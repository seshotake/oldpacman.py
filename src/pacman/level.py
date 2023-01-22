import pygame

from entities.player import Player
from entities.wall import Wall
from pacman.settings import *
from pacman.camera import YSortCameraGroup
from pacman.ui import UI


class Level:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # generate level
        self.generate()

        # User Interface
        self.ui = UI()

    # generate level
    def generate(self) -> None:
        for row_index, row in enumerate(LEVEL_MAP):
            for col_index, col in enumerate(row):
                x, y = col_index * WALL_SIZE, row_index * WALL_SIZE
                if col == 'x':
                    Wall(position=(x, y), groups=[
                         self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = Player(position=(x, y), groups=[
                                         self.visible_sprites], obstacle_sprites=self.obstacle_sprites)

    def draw(self) -> None:
        self.visible_sprites.custom_draw(self.player)

    def update(self) -> None:
        self.visible_sprites.update()
        self.ui.display(self.player)
