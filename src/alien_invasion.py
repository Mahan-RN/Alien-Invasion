import sys
from time import sleep
import pygame
from pygame.event import Event
from pygame.sprite import Group


from settings import Settings
from game_stats import GameStats
import space_ship as ss
from bullet import Bullet
from alien import Alien
from button import Button


class AlienInvasion:
    """Overall class to merge game assets and behvaior"""

    def __init__(self) -> None:
        """Initialize the game, and create game resources"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.settings.width = self.screen.get_rect().width
        self.settings.height = self.screen.get_rect().height
        self.image = pygame.image.load(
            "src/resources/images/game_background.png"
        ).convert()
        self.image = pygame.transform.scale(
            self.image, (self.settings.width, self.settings.height)
        )
        self.clock = pygame.time.Clock()
        self.ship = ss.Ship(self)
        self.bullets = Group()
        self.aliens = Group()

        self._create_fleet()
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        # Start Alien Invasion game in an inactive state
        self.game_active: bool = False

        # Make the play button
        self.play_button = Button(self, "Play")

    def run_game(self) -> None:
        """Start the main loop for the game"""
        while True:
            self._check_events()
            if self.game_active:
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos) -> None:
        """Start a new game when the play clicks play"""
        button_clicked: bool = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            # Reset the game statistics
            self.stats.reset_stats()
            self.game_active = True
            # Get rid of any remaining bullets and aliens
            self.aliens.empty()
            self.bullets.empty()
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            # Hide mouse cursor
            pygame.mouse.set_visible(False)

    def _update_screen(self) -> None:
        """Update images on the screen and filp to the new screen"""
        self.screen.blit(self.image, (0, 0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the play button if the game is inactive
        if not self.game_active:
            self.play_button.draw_button()
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
        self._check_bullet_alien_collisions()

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

    def _create_alien(self, x_position: int, y_position: int) -> None:
        """Create an alien and place it in the row"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self) -> None:
        """Respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self) -> None:
        """Update the position of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):  # type: ignore
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _check_bullet_alien_collisions(self) -> None:
        """Respond to bullet-alien collisions"""
        # Remove any bullets and alies that have collided
        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        # Destroy existing bullets and create new fleet if all aliens are
        # destroyed
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    ## Helpers for alien-ship collisions
    def _ship_hit(self) -> None:
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            # Decrement ships left
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    ## Helper for when alien(s) reach bottom of the screen
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.height:
                # Treat this the same as if the ship got hit
                self._ship_hit()
                break


if __name__ == "__main__":
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
