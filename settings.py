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
        self.cat_limit = 3

        # Cheese settings
        self.cheese_speed = 1.5
        self.cheese_width = 3
        self.cheese_height = 15
        self.cheese_allowed = 20

        # Mouse settings
        self.mouse_speed = 1.0
        self.mouse_drop_speed = 10
        # mouse direction of 1 reprsents right; -1 represents left
        self.mouse_direction = 1
       