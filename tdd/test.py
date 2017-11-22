"""test"""
import unittest
from game import Game

class TestBowling(unittest.TestCase):
    """class"""
    def setUp(self):
        """set up"""
        self.game = Game()

    def test_all_ones(self):
        """
        If you don't get a strike or a spare, then you just add up the face
        value of the frame. In this case, each frame is worth one point, so
        the total is eleven.
        """
        pins = [1 for i in range(11)]
        self.game.roll(11, pins)
        self.assertEqual(self.game.score, 11)

    def test_strike(self):
        """
        A strike is 10 + the value of the next two rolls. So in this
        cas, the first frame will be 10+5+4 or 19 and the second will be
        5+4, the total score would be 19+9 or 28.
        """
        self.game.roll(11, [10, 5, 4])
        self.assertEqual(self.game.score, 28)
if __name__ == '__main__':
    unittest.main()
