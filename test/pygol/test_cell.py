from pygol import cell

import unittest

class TestCell(unittest.TestCase):

    def test_can_be_alive(self):
        c = cell.LiveCell()
        self.assertEquals(cell.Alive, c.mortality)

    def test_can_be_dead(self):
        c = cell.DeadCell()
        self.assertEquals(cell.Dead, c.mortality)
     
