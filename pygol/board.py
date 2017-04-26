import cell

class Board(object):

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height
        self.cells = [[cell.DeadCell() for x in range(width)] for y in range(height)]
    
    def setCellAt(self, x, y, cell):
        self.cells[y][x] = cell

    def cellAt(self, x, y):
        return self.cells[y][x]

