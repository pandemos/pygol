from pygol import board
from pygol import cell
from pygol import board_format as BF

import unittest

class TestPlaintextBoardFormat(unittest.TestCase):

    def test_header_serialization(self):
        """ A header is serialized as `!Name: "name"` followed by a line containing only `!` """

        self.assertEquals(BF.PlaintextHeaderFormat(name="Example").serialize(), "!Name: Example\n!\n")

    def test_living_cell_serialization(self):
        """ A living cell is serialized by `O` (capital letter 'o') """
        self.assertEquals(BF.PlaintextCellFormat(cell.LiveCell()).serialize(), "O")

    def test_dead_cell_serialization(self):
        """ A dead cell is serialized as a `.` """
        self.assertEquals(BF.PlaintextCellFormat(cell.DeadCell()).serialize(), ".")

    def test_board_serialization(self):
        """ A board is serialized as a header followed by visually-representative cells """

        b = board.Board(width=3, height=3)
        b.setCellAt(1, 0, cell.LiveCell())
        b.setCellAt(2, 1, cell.LiveCell())
        b.setCellAt(0, 2, cell.LiveCell())
        b.setCellAt(1, 2, cell.LiveCell())
        b.setCellAt(2, 2, cell.LiveCell())
        self.assertEquals(BF.PlaintextBoardFormat(b, "name").serialize(), "!Name: name\n!\n.O.\n..O\nOOO\n")
