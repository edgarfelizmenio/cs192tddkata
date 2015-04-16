import unittest
import bowling

class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.game = bowling.Game()

    def testGutterGame(self):
        for i in range(20):
            self.game.roll(0)

        self.assertEqual(0, self.game.score())

    def testAllOnes(self):
        for i in range(20):
            self.game.roll(1)

        self.assertEqual(20, self.game.score())

unittest.main()
