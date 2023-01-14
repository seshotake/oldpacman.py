import pygame

from entities.entity import Entity


class Player(Entity):
    def __init__(self, **kwargs) -> None:
        kwargs["asset_path"] = "assets/player.png"
        kwargs["speed"] = 5
        super().__init__(**kwargs)

    def input(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self) -> None:
        self.input()
        self.move(self.speed)
