import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """Represents a bullet shot by the spaceship in the game"""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.image = pygame.image.load("src/resources/images/space_ship_image.png")
        self.rect = self.image.get_rect()

        # Set bullet's midpoint to the midpoint of the spaceship
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the bullet up the screen"""
        # Update the exact position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = int(self.y)

    def draw_bullet(self) -> None:
        """Draw the bullet to the screen"""
        self.screen.blit(self.image, self.rect)
