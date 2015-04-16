class Game(object):

    def __init__(self):
        self.gamescore = 0

    def roll(self, pins):
        self.gamescore += pins

    def score(self):
        return self.gamescore
