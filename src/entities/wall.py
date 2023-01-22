import pygame

from entities.entity import Entity


class Wall(Entity):
    def __init__(self, **kwargs) -> None:
        kwargs["asset_path"] = "assets/images/wall.png"
        super().__init__(**kwargs)
