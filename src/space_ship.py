import pygame

from alien_invasion import AlienInvasion


class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game: AlienInvasion) -> None:
        """Initialize the ship and set its starting position

        Args:
            ai_game (AlienInvasion): an instance of the main game
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load("src/resources/images/space_ship_image.png")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Movement flag; start with a ship that's not moving
        self.moving_right: bool = False
        self.moving_left: bool = False


    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag
        """        
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
