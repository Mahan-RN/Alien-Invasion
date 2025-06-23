import sys
import pygame
from pygame.event import Event
from pygame.sprite import Group

from settings import Settings
import space_ship as ss
from bullet import Bullet
from alien import Alien


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
        self.bullets = Group()
        self.aliens = Group()

        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")

    def run_game(self) -> None:
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    ## Helpers for running the game
    def _check_events(self) -> None:
        """Respond to key and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self) -> None:
        """Update images on the screen and filp to the new screen"""
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.BACKGROUND_COLOR)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible
        pygame.display.flip()

    ## Helpers for game controls
    def _check_keydown_events(self, event: Event) -> None:
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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event: Event) -> None:
        """Respond to key releases

        Args:
            event (Event): KEYUP event
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    ## Helpers for bullets
    def _fire_bullet(self) -> None:
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self) -> None:
        """Update position of bullets and get rid of old bullets"""
        # Update bullet positions
        self.bullets.update()

        # Get ridd of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    ## Helpers for aliens
    def _create_fleet(self) -> None:
        """Create the fleet of aliens"""
        # Create an alien and keep adding aliens until there's no room left
        # Spacing between aliens is one alien width and one alien height
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.height - 16 * alien_height):
            while current_x < (self.settings.width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x-value, and increment y-value
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position: int, y_position: int):
        """Create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _update_aliens(self):
        """Update the position of all aliens in the fleet"""
        self.aliens.update()


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
