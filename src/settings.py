from typing import Final


class Settings:

    def __init__(self) -> None:
        """A class to store all settings of the game"""
        
        # Screen Settings
        self.width: int
        self.height: int
        self.ship_speed: Final[float] = 6.5
        # Bullet settings
        self.bullet_speed: float = 8.0
        self.bullets_allowed = 25
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1