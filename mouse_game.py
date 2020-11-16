
import sys

import pygame

from settings import Settings
from cat import Cat

class MouseGame:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Macka Mouse Game")

        self.cat = Cat(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.cat.update()
            self._update_screen()

    def _check_events(self):
        # Responds to keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.cat.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.cat.moving_left = True
        if event.key == pygame.K_UP:
            self.cat.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.cat.moving_down = True

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.cat.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.cat.moving_left = False
        if event.key == pygame.K_UP:
            self.cat.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.cat.moving_down = False
    
    def _update_screen(self):
         # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.cat.blitme()
        # Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game
    mg = MouseGame()
    mg.run_game()