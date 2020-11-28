import pygame

class Cat:
    """A class to manage the cat"""
    def __init__(self, mg_game):
        """Initialize cat and it's starting position"""
        self.screen = mg_game.screen
        self.settings = mg_game.settings
        self.screen_rect = mg_game.screen.get_rect()

        # Load cat image and get it's rect
        self.image = pygame.image.load('mouse_game/image/cat1.png')
        self.rect = self.image.get_rect()

        # Start each cat at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal for the cat's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False 

    
    def update(self):
        """Update cat's position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.cat_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.cat_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.cat_speed 
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.cat_speed
            

        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def center_cat(self):
        """ Center the cat on the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the cat at its current location"""
        self.screen.blit(self.image, self.rect)
