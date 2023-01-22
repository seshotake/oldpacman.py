import pygame

from pacman.settings import *
from entities.player import Player


class UI:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        self.health_bar = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)

    def show_bar(self, current: int, max_amount: int, background_rect: pygame.rect.Rect, color: str) -> None:
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, background_rect)

        ratio = current / max_amount
        current_width = background_rect.width * ratio
        current_rect = background_rect.copy()
        current_rect.width = int(current_width)

        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, current_rect, 1)


    def display(self, player: Player) -> None:
        self.show_bar(
            player.health, player.max_health, self.health_bar, HEALTH_BAR_COLOR)
