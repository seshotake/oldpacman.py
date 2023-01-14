import pygame

from entities.entity import Entity


class Wall(Entity):
    def __init__(self, **kwargs) -> None:
        if kwargs.get("asset_path") is None:
            kwargs["asset_path"] = "assets/wall.png"
        super().__init__(**kwargs)
