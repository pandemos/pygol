from pygol.board_format import RleHeaderFormat
from pygol.board_format import RleCellFormat
from pygol.board_format import RleRowFormat
from pygol.board_format import RleBoardFormat

from pygol import cell
from pygol import board

import unittest

class TestRleBoardFormat(unittest.TestCase):

    def test_header_serialization(self):
        self.assertEquals(RleHeaderFormat(width=3, height=4, rule="B3/S23").serialize(), "x = 3, y = 4, rule = B3/S23\n")

    def test_living_cell_serialization(self):
        self.assertEquals(RleCellFormat(cell.LiveCell()).serialize(), "o")

    def test_dead_cell_serialization(self):
        self.assertEquals(RleCellFormat(cell.DeadCell()).serialize(), "b")
    
    def test_row_serialization_direct(self):
        b = board.Board(width = 3, height = 1)
        b.set_cell_at(0, 0, cell.LiveCell())
        b.set_cell_at(2, 0, cell.LiveCell())
        self.assertEqual(RleRowFormat(b, 0).serialize(), "obo$")

    def test_last_row_serialization_direct(self):
        b = board.Board(width = 3, height = 1)
        b.set_cell_at(0, 0, cell.LiveCell())
        b.set_cell_at(2, 0, cell.LiveCell())
        self.assertEqual(RleRowFormat(b, 0, last=True).serialize(), "obo!")

    def test_row_serialization_collapsed(self):
        b = board.Board(width=3, height=1)
        b.set_cell_at(1, 0, cell.LiveCell())
        b.set_cell_at(2, 0, cell.LiveCell())
        self.assertEquals(RleRowFormat(b, 0).serialize(), "b2o$")

        b.setCellAt(0, 0, cell.LiveCell())
        b.setCellAt(1, 0, cell.LiveCell())
        b.setCellAt(2, 0, cell.LiveCell())
        self.assertEquals(RleRowFormat(b, 0).serialize(), "3o$")

    def test_row_serialization_drops_trailing_dead_cells(self):
        b = board.Board(width=3, height=1)
        b.set_cell_at(0, 0, cell.LiveCell())
        self.assertEquals(RleRowFormat(b, 0).serialize(), "o$")

    def test_board_serialization(self):
        b = board.Board(width=3, height=3)
        b.set_cell_at(1, 0, cell.LiveCell())
        b.set_cell_at(2, 1, cell.LiveCell())
        b.set_cell_at(0, 2, cell.LiveCell())
        b.set_cell_at(1, 2, cell.LiveCell())
        b.set_cell_at(2, 2, cell.LiveCell())
        self.assertEquals(RleBoardFormat(b).serialize(), "x = 3, y = 3, rule = B3/S23\nbo$2bo$3o!")
