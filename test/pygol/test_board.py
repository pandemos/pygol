from pygol import board
from pygol import cell

import unittest

class TestBoard(unittest.TestCase):

    def test_has_width_and_height(self):
        """ A board is primarily specified by its width and height """

        b = board.Board(width=10, height=10)
        self.assertEquals(b.width, 10)
        self.assertEquals(b.height, 10)

    def test_can_retrieve_cell_by_coordinate(self):
        """ Any cell can be retrieved from the board by specifying an x and y coordinate """

        c = cell.LiveCell()
        b = board.Board(width=10, height=10)

        # Living cell
        b.setCellAt(x=3, y=3, cell=c)
        self.assertEquals(b.cellAt(3, 3), c)

        # Dead cell
        self.assertEquals(b.cellAt(7, 7).mortality, cell.Dead)

    def test_iteration_count_starts_at_zero(self):
        """ Iteration count starts at 0 """
        b = board.Board(width=10, height=10)
        self.assertEquals(b.iteration, 0)

    def test_has_iteration_count(self):
        """ Board has an iteration count """
        
        b = board.Board(width=10, height=10, iteration=4)
        self.assertEquals(b.iteration, 4)

    def test_iteration_count_can_be_incremented(self):
        """ Iteration count can be incremented """

        b = board.Board(width=10, height=10)
        self.assertEquals(b.iteration, 0)
        b.step()
        self.assertEquals(b.iteration, 1)
        b.step()
        self.assertEquals(b.iteration, 2)

    def test_iteration_count_can_be_reset(self):
        """ Iteration count can be reset """

        b = board.Board(width=10, height=10, iteration=4)
        b.reset()
        self.assertEquals(b.iteration, 0)

    def test_out_of_range_cell(self):
        """ Attempt to access a cell outside the board throws an exception """

        b = board.Board(width=10, height=10)
        
        with self.assertRaises(IndexError):
            b.setCellAt(-1, -1, cell.LiveCell())
        with self.assertRaises(IndexError):
            b.cellAt(-1, -1)
        with self.assertRaises(IndexError):
            b.cellAt(b.width, b.height)

    def test_determine_number_of_living_zero_neighbors(self):
        """ For any cell, determine the number of living neighbors when no neighbors are living """

        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 0)

    def test_determine_number_of_living_one_neighbor_edges(self):
        """ For any cell, determine the number of living neighbors when one edge neighbor is living """

        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(1, 0, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 1)

        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(0, 1, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 1)

        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(2, 1, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 1)

        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(1, 2, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 1)

    def test_determine_number_of_living_two_neighbor_edges(self):
        """ For any cell, determine the number of living neighbors when one edge neighbor is living """

        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(1, 0, cell.LiveCell())
        b.setCellAt(0, 1, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 2)

        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(2, 1, cell.LiveCell())
        b.setCellAt(1, 2, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 2)

    def test_determine_number_of_living_one_neighbor_corner(self):
        """ For any cell, determine the number of living neighbors when one corner neighbor is living """

        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(0, 0, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 1)
        
        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(0, 2, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 1)
        
        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(2, 0, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 1)
        
        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(2, 2, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 1)
        
    def test_determine_number_of_living_two_neighbor_corner(self):
        """ For any cell, dtermine the number of living neighbors when two corner neighbors are living """

        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(0, 0, cell.LiveCell())
        b.setCellAt(2, 2, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 2)

        b = board.Board(width=3, height=3)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(2, 0, cell.LiveCell())
        b.setCellAt(0, 2, cell.LiveCell())
        self.assertEquals(b.livingNeighbors(1, 1), 2)

