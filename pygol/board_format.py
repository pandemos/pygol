import cell
from board import Board

class PlaintextHeaderFormat(object):

    def __init__(self, name):
        self.name = name

    def serialize(self):
        return "!Name: {}\n!\n".format(self.name)

class PlaintextCellFormat(object):

    def __init__(self, cell):
        self.cell = cell

    def serialize(self):
        if self.cell.mortality == cell.Alive:
            return "O"
        elif self.cell.mortality == cell.Dead:
            return "."

class PlaintextBoardFormat(object):
    def __init__(self, board, name):
        self.board = board
        self.name = name

    def serialize(self):
        serialize_row = lambda y: ''.join([PlaintextCellFormat(self.board.cellAt(x, y)).serialize() for x in range(self.board.width)]) 
        result = [serialize_row(y) for y in range(self.board.height)]
        
        return PlaintextHeaderFormat(self.name).serialize()+'\n'.join(result)+'\n'

class RleHeaderFormat(object):
    def __init__(self, width, height, rule):
        self.width = width
        self.height = height
        self.rule = rule

    def serialize(self):
        return "x = {0}, y = {1}, rule = {2}\n".format(self.width, self.height, self.rule)

class RleCellFormat(object):
    def __init__(self, cell):
        self.cell = cell

    def serialize(self):
        if self.cell.mortality is cell.Alive:
            return "o"
        else:
            return "b"

class RleRowFormat(object):
    def __init__(self, b, y, last=False):
        self.board = b
        self.y = y
        self.last = last

    def serialize(self):
        result = []

        for x in range(self.board.width):
            this_cell = self.board.cell_at(x, self.y)
            next_cell = self.board.cell_at(x+1, self.y) if x < self.board.width-1 else None
            result.append(RleCellFormat(this_cell).serialize())

        endchar = '!' if self.last else '$'
        return ''.join(result) + endchar

