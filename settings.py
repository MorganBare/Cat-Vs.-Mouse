class Settings:
    """A class to store all settings for Mouse game"""

    def __init__(self):
        """Initialize the game's static settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (121, 164, 182)

        # Cat settings
        self.cat_limit = 3

        # Cheese settings
        self.cheese_width = 3
        self.cheese_height = 15
        self.cheese_allowed = 20

        # Mouse settings
        self.mouse_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initialize the settings that chnage throughout the game
        self.cat_speed = 1.5
        self.cheese_speed = 3.0
        self.mouse_speed = 1.0

        # mouse direction of 1 reprsents right; -1 represents left
        self.mouse_direction = 1

    def increase_speed(self):
        # increase speed settings
        self.cat_speed *= self.speedup_scale
        self.cheese_speed *= self.speedup_scale
        self.mouse_speed *= self.speedup_scale
       