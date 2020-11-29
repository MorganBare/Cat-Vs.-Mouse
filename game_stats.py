

class GameStats:
    """ Tracks statistics for Mouse Game """
    def __init__(self, mg_game):
        """ Initialize stats """
        self.settings = mg_game.settings 
        self.reset_stats()

        # Start Mouse Game in an active state
        self.game_active = False

        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """ Initialize the stats that can change during the game """
        self.cats_left = self.settings.cat_limit
        self.score = 0