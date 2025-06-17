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
        self.bullet_speed: float = 2.0
        self.bullet_width: int = 3
        self.bullet_height: int = 15
        self.bullet_color: tuple[int, int, int] = (60, 60, 60)
