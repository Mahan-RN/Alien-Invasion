from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game: "AlienInvasion") -> None:
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score: int = 0

    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score: int = 0
