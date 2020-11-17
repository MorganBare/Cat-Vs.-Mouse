import pygame
from pygame.sprite import Sprite

class Cheese(Sprite):
    """A class to manage the cheese fired from the cat"""

    def __init__(self, mg_game):
        """Create a cheese object at cat's current position"""
        super().__init__()
        self.screen = mg.screen
        self.settings = mg_game.settings 
        self.color = self.settings.cheese_color

        # Create a cheese rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.cheese_width, self.settings.cheese_height)
        self.rect.midtop = mg_game.cat.rect.midtop

        # Store cheese position as a decimal value
        self.y = float(self.rect.y)

