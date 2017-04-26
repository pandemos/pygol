from pygol import board
from pygol import cell

import unittest

class TestBoard(unittest.TestCase):

    def test_has_width_and_height(self):
        b = board.Board(width = 10, height = 10)
        self.assertEquals(b.width, 10)
        self.assertEquals(b.height, 10)

    def test_can_retrieve_cell_by_coordinate(self):
        c = cell.LiveCell()
        b = board.Board(width = 10, height = 10)

        # Living cell
        b.setCellAt(x = 3, y = 3, cell = c)
        self.assertEquals(b.cellAt(3, 3), c)

        # Dead cell
        self.assertEquals(b.cellAt(7, 7).mortality, cell.Dead)


