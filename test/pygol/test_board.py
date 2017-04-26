from pygol import board

import unittest

class TestBoard(unittest.TestCase):

    def test_has_width_and_height(self):
        b = board.Board(width = 10, height = 10)
        self.assertEquals(b.width, 10)
        self.assertEquals(b.height, 10)

