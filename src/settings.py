from typing import Final


class Settings:

    def __init__(self) -> None:
        """A class to store all settings of the game"""
        
        # Screen Settings
        self.width: int
        self.height: int
        self.BACKGROUND_COLOR: Final[tuple[int, int, int]] = (230, 230, 230)
        self.ship_speed: Final[float] = 6.5
        # Bullet settings
        self.bullet_speed: float = 8.0
        self.bullets_allowed = 25
        # Alien settings
        self.alien_speed = 1.0