class Settings:
    """A class to store all settings of the game"""

    def __init__(self) -> None:
        """Initialize the game's static settings"""
        # Screen settings
        self.width: int
        self.height: int
        # Ship settings
        self.ship_limit: int = 3
        # Bullet settings
        self.bullets_allowed: int = 25
        # Alien settings
        self.fleet_drop_speed: int = 10
        # How quickly the game speeds up
        self.speedup_scale: float = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed: float = 6.5
        self.bullet_speed: float = 8.0
        self.alien_speed: float = 1.0
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction: int = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

