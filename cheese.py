import pygame
from pygame.sprite import Sprite
from pygame.locals import RLEACCEL

class Cheese(Sprite):
    """A class to manage the cheese fired from the cat"""

    def __init__(self, mg_game):
        """Create a cheese object at cat's current position"""
        super().__init__()
        self.screen = mg_game.screen
        self.settings = mg_game.settings 

        # Load cheese image and get it's rect
        self.image = pygame.image.load('mouse_game/image/cheese.png').convert()
        self.rect = self.image.get_rect()

        # Create a cheese rect at (0,0) and then set correct position
        #self.rect = pygame.Rect(0, 0, self.settings.cheese_width, self.settings.cheese_height)
        self.rect.midtop = mg_game.cat.rect.midtop

        # Store cheese position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the cheese up the screen"""
        # Update decimal point of the cheese
        self.y -= self.settings.cheese_speed
        # Update the rect position
        self.rect.y = self.y

    def blt_cheese(self):
        """Draw the cheese at its current location"""
        self.screen.blit(self.image, self.rect)
