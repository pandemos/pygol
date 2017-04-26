import cell

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
