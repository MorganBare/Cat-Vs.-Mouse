import pygame
from pygame.sprite import Sprite

class Mouse(Sprite):
    """A Class to represent a single mouse in the pack"""

    def __init__(self, mg_game):
        # Initialize the mouse and set it's starting position
        super().__init__()
        self.screen = mg_game.screen
        self.settings = mg_game.settings

        # Load the mouse image and set its rect attribute
        self.image = pygame.image.load('mouse_game/image/mouse.png')
        self.rect = self.image.get_rect()

        # Start each new mouse near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Stoe the mouse's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if mouse is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move mice to the right"""
        self.x += (self.settings.mouse_speed * self.settings.mouse_direction)
        self.rect.x = self.x