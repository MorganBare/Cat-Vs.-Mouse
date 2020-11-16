import pygame

class Cat:
    """A class to manage the cat"""
    def __init__(self, mg_game):
        """Initialize cat and it's starting position"""
        self.screen = mg_game.screen
        self.screen_rect = mg_game.screen.get_rect()

        # Load cat image and get it's rect
        self.image = pygame.image.load('images/cat.png')
        self.rect = self.image.get_rect()

        # Start each cat at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
    
    def update(self):
        """Update cat's position based on movement flag"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw the cat at its current location"""
        self.screen.blit(self.image, self.rect)
