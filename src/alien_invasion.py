import sys
import pygame
from typing import Final


class AlienInvasion:
    """Overall class to merge game assets and behvaior"""

    def __init__(self) -> None:
        """Initialize the game, and create game resources"""
        pygame.init()

        # Constants
        self.WIDTH: Final[int] = 1200
        self.HEIGHT: Final[int] = 800
        self.BACKGROUND_COLOR: Final[tuple[int, int, int]] = (230, 230, 230)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Alien Invasion")

    def run_game(self) -> None:
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Redraw the screen during each pass through the loop
            self.screen.fill(self.BACKGROUND_COLOR)

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
