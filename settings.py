class Settings:
    """A class to store all settings for Mouse game"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (121, 164, 182)

        # Cat settings
        self.cat_speed = 1.5

        # Cheese settings
        self.cheese_speed = 1.0
        self.cheese_width = 3
        self.cheese_height = 15
        self.cheese_color = (60, 60, 60)