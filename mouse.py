import pygame
from pygame.sprite import Sprite

class Mouse(Sprite):
    """A Class to represent a single mouse in the pack"""

    def __init__(self, mg_game):
        # Initialize the mouse and set it's starting position
        super().__init__()
        self.screen = mg_game.screen

        # Load the mouse image and set its rect attribute
        self.image = pygame.image.load('mouse_game/image/mouse.png')
        self.rect = self.image.get_rect()

        # Start each new mouse near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Stoe the mouse's exact horizontal position
        self.x = float(self.rect.x)