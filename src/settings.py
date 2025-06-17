from typing import Final

class Settings:

    def __init__(self) -> None:
        """A class to store all settings of the game"""
        # Screen Settings
        self.WIDTH: Final[int] = 1200
        self.HEIGHT: Final[int] = 800
        self.BACKGROUND_COLOR: Final[tuple[int, int, int]] = (230, 230, 230)
        self.ship_speed: Final[float] = 6.5
