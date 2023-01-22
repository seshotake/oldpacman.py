from enum import Enum
import pygame


class Entity(pygame.sprite.Sprite):
    rect: pygame.rect.Rect

    class Direction(Enum):
        HORIZONTAL = 0
        VERTICAL = 1

    def __init__(self, **kwargs) -> None:
        super().__init__(*kwargs.get("groups", []))

        self.image = pygame.image.load(kwargs["asset_path"]).convert_alpha()
        self.rect = self.image.get_rect(topleft=kwargs["position"])

        self.frame_index: int = kwargs.get("frame_index", 0)
        self.animation_speed: int = kwargs.get("animation_speed", 0)
        self.speed: int = kwargs.get("speed", 0)
        self.direction = pygame.math.Vector2(0, 0)
        
        self.obstacle_sprites: list[Entity] = kwargs.get(
            "obstacle_sprites", None)

        self.max_health: int = kwargs.get("max_health", 0)
        self.health = kwargs.get("health", 0)

    def move(self, speed: int) -> None:
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += int(self.direction.x * speed)
        self.collision(self.Direction.HORIZONTAL)
        self.rect.y += int(self.direction.y * speed)
        self.collision(self.Direction.VERTICAL)

    def collision(self, direction: Direction) -> None:
        if self.obstacle_sprites is None:
            return

        for sprite in self.obstacle_sprites:
            if sprite.rect is None:
                return

            if sprite.rect.colliderect(self.rect):
                match direction:
                    case Entity.Direction.HORIZONTAL:
                        if self.direction.x > 0:
                            self.rect.right = sprite.rect.left
                        if self.direction.x < 0:
                            self.rect.left = sprite.rect.right
                    case Entity.Direction.VERTICAL:
                        if self.direction.y > 0:
                            self.rect.bottom = sprite.rect.top
                        if self.direction.y < 0:
                            self.rect.top = sprite.rect.bottom
