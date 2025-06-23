from typing import Final


class Settings:

    def __init__(self) -> None:
        """A class to store all settings of the game"""

        # Screen settings
        self.width: int
        self.height: int
        # Ship settings
        self.ship_speed: Final[float] = 6.5
        self.ship_limit: int = 3
        # Bullet settings
        self.bullet_speed: float = 8.0
        self.bullets_allowed: int = 25
        # Alien settings
        self.alien_speed: float = 1.0
        self.fleet_drop_speed: int = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction: int = 1
