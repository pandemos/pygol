from rule_formats import RleRuleFormat
import board
import cell

class Rules(object):

    def apply_rules(self, b, new_board, x, y, c):
        for rule in self.rule_format.birth_neighbors:
            if c.is_dead() and b.living_neighbors(x, y) == int(rule):
                new_board.set_cell_at(x, y, cell.LiveCell())

        n_neighbors = b.living_neighbors(x, y)
        matches_rule = n_neighbors in [int(r) for r in self.rule_format.sustain_neighbors]
        if c.is_alive() and matches_rule:
            new_board.set_cell_at(x, y, cell.LiveCell())

    def apply_to(self, b):
        new_board = board.Board(b.width, b.height, b.iteration, b.rules)

        b.for_each(lambda x, y, c: self.apply_rules(b, new_board, x, y, c))

        b.cells = new_board.cells

class ConwayRules(Rules):
    def __init__(self):
        self.rule_string = "B3/S23"
        self.rule_format = RleRuleFormat(self.rule_string)

class GenericRules(Rules):

    def __init__(self, rule_string):
        self.rule_string = rule_string
        self.rule_format = RleRuleFormat(self.rule_string)
