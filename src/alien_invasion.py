import sys
import pygame
from pygame.event import Event

from settings import Settings
import space_ship as ss


class AlienInvasion:
    """Overall class to merge game assets and behvaior"""

    def __init__(self) -> None:
        """Initialize the game, and create game resources"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.width = self.screen.get_rect().width
        self.settings.height = self.screen.get_rect().height
        self.clock = pygame.time.Clock()
        self.ship = ss.Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self) -> None:
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to key and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """Update images on the screen and filp to the new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.BACKGROUND_COLOR)
        self.ship.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _check_keydown_events(self, event: Event):
        """Respond to key presses

        Args:
            event (Event): KEYDOWN event
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event: Event):
        """Respond to key releases

        Args:
            event (Event): KEYUP event
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
