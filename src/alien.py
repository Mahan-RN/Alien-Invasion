import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game: "AlienInvasion", *groups) -> None:
        super().__init__(*groups)
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute
        self.image = pygame.image.load("src/resources/images/alien_image.png")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = int(self.x)
