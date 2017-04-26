from pygol import board
from pygol import cell
from pygol import rules

import unittest

class TestRules(unittest.TestCase):

    def test_can_be_applied(self):
        """ Rules can be applied """

        r = rules.ConwayRules()
        r.apply_to(board.Board(0, 0))
        
    def test_configured_via_rulestring(self):
        """ Rules are configured via rulestring """

        rule_string = "B3/S23"
        r = rules.GenericRules(rule_string = rule_string)
        self.assertEquals(r.rule_string, rule_string)

class TestConwayRules(unittest.TestCase):

    def test_living_cell_dies_with_zero_neighbors(self):
        """ A living cell dies if it has 0 living neighbors """
        
        b = board.Board(width=5, height=5)
        b.setCellAt(2, 2, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_dead())
    
    def test_living_cell_dies_with_one_neighbor(self):
        """ A living cell dies it it has 1 living neighbors """

        b = board.Board(width=5, height=5)
        b.setCellAt(2, 2, cell.LiveCell())
        b.setCellAt(2, 1, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_dead())

        b = board.Board(width=5, height=5)
        b.setCellAt(2, 2, cell.LiveCell())
        b.setCellAt(1, 1, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_dead())

        b = board.Board(width=5, height=5)
        b.setCellAt(2, 2, cell.LiveCell())
        b.setCellAt(1, 2, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_dead())

        b = board.Board(width=5, height=5)
        b.setCellAt(2, 2, cell.LiveCell())
        b.setCellAt(1, 3, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_dead())

        b = board.Board(width=5, height=5)
        b.setCellAt(2, 2, cell.LiveCell())
        b.setCellAt(2, 3, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_dead())

        b = board.Board(width=5, height=5)
        b.setCellAt(2, 2, cell.LiveCell())
        b.setCellAt(3, 1, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_dead())

        b = board.Board(width=5, height=5)
        b.setCellAt(2, 2, cell.LiveCell())
        b.setCellAt(3, 2, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_dead())

        b = board.Board(width=5, height=5)
        b.setCellAt(2, 2, cell.LiveCell())
        b.setCellAt(3, 3, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_dead())

    def test_living_cell_dies_with_four_neighbors(self):
        """ A living cell dies if it has four living neighbors """
        
        b = board.Board(width=5, height=5)
        b.setCellAt(2, 2, cell.LiveCell())
        b.setCellAt(2, 1, cell.LiveCell())
        b.setCellAt(2, 3, cell.LiveCell())
        b.setCellAt(1, 2, cell.LiveCell())
        b.setCellAt(3, 2, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_dead())

        b = board.Board(width=5, height=5)
        b.setCellAt(2, 2, cell.LiveCell())
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(1, 3, cell.LiveCell())
        b.setCellAt(3, 1, cell.LiveCell())
        b.setCellAt(3, 3, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_dead())

    def test_cell_is_born_with_exactly_three_neighbors(self):
        """ A cell is born if it has exactly three living neighbors """

        b = board.Board(width=5, height=5)
        b.setCellAt(2, 1, cell.LiveCell())
        b.setCellAt(2, 3, cell.LiveCell())
        b.setCellAt(1, 2, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_alive())

        b = board.Board(width=5, height=5)
        b.setCellAt(1, 1, cell.LiveCell())
        b.setCellAt(1, 3, cell.LiveCell())
        b.setCellAt(3, 3, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_alive())

    def test_spinner(self):
        """ Both phases of a three-cell spinner are born and die appropriately """

        b = board.Board(width=5, height=5)
        b.setCellAt(1, 2, cell.LiveCell())
        b.setCellAt(2, 2, cell.LiveCell())
        b.setCellAt(3, 2, cell.LiveCell())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_alive())
        self.assertTrue(b.cellAt(2, 1).is_alive())
        self.assertTrue(b.cellAt(2, 3).is_alive())
        self.assertTrue(b.cellAt(1, 2).is_dead())
        self.assertTrue(b.cellAt(3, 2).is_dead())
        b.step()
        self.assertTrue(b.cellAt(2, 2).is_alive())
        self.assertTrue(b.cellAt(2, 1).is_dead())
        self.assertTrue(b.cellAt(2, 3).is_dead())
        self.assertTrue(b.cellAt(1, 2).is_alive())
        self.assertTrue(b.cellAt(3, 2).is_alive())
