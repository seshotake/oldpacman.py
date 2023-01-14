import pygame

from entities.player import Player


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.half_width, self.half_height = [
            side / 2 for side in self.display_surface.get_size()]
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player: Player) -> None:
        self.offset = self.get_offset(player)

        for sprite in sorted(self.sprites(),
                             key=lambda sprite: sprite.rect.centery):  # type: ignore[union-attr]
            if sprite.rect is None or sprite.image is None:
                continue

            offset_position = sprite.rect.topleft + \
                self.offset  # type: ignore[operator]
            self.display_surface.blit(sprite.image, offset_position)

    def get_offset(self, player: Player) -> pygame.math.Vector2:
        """Get the offset of the camera based on the player's position."""

        if player.rect is None:
            return pygame.math.Vector2(0, 0)

        return pygame.math.Vector2(self.half_width - player.rect.centerx, self.half_height - player.rect.centery)
