import unittest
from app.bowling_game import Game

class BowlingGameTest(unittest.TestCase):
    # execute before every test
    def setUp(self):
        self.g = Game()

    # helper functions
    def roll_many(self, n, pins):
        for i in range(0, n):
            self.g.roll(pins)

    def roll_spare(self):
        self.g.roll(5)
        self.g.roll(5)

    def roll_strike(self):
        self.g.roll(10)

    # 1st Test
    def test_gutter_game(self):
        self.roll_many(20, 0)
        self.assertEqual(0, self.g.score())

    # 2nd Test
    def test_all_ones(self):
        self.roll_many(20, 1)
        self.assertEqual(20, self.g.score())

    # 3rd Test
    def test_one_spare(self):
        self.roll_spare()
        self.g.roll(3) # spare bonus
        self.roll_many(17, 0)
        self.assertEqual(16, self.g.score())

    # 4th Test
    def test_one_strike(self):
        self.roll_strike()
        self.g.roll(3) # spare bonus
        self.g.roll(4) # spare bonus
        self.roll_many(16, 0)
        self.assertEqual(24, self.g.score())

    # 5th Test
    def test_perfect_game(self):
        for i in range(0, 12):
            self.g.roll(10)
        self.assertEqual(300, self.g.score())

if __name__ == '__main__':
    unittest.main()