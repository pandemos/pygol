import cell
import rules

class Board(object):

    def __init__(self, width = 0, height = 0, iteration=0, rules=None):
        self.width = width
        self.height = height
        self.rules = rules

        # Good example of this approach working:
        # I had initially forgotten to change this from `= 0` to `= iteration`
        # Without the specific test, even though this is merely an assignment,
        # that might have survived much longer.
        self.iteration = iteration

        self.cells = [[cell.DeadCell() for x in range(width)] for y in range(height)]
    
    def setCellAt(self, x, y, cell):
        """ Deprecated """
        return self.set_cell_at(x, y, cell)

    def set_cell_at(self, x, y, cell):

        # We don't observe the magical Python indexing here. x and y must be absolute
        # indices into the board.
        if y < 0 or y >= self.height or x < 0 or x >= self.width:
            raise IndexError("Attempt to set cell at invalid position {0},{1}", [x, y])

        self.cells[y][x] = cell

    def cellAt(self, x, y):
        """ Deprecated """
        return self.cell_at(x, y)

    def cell_at(self, x, y):

        # We don't observe the magical Python indexing here. x and y must be absolute
        # indices into the board.
        if y < 0 or y >= self.height or x < 0 or x >= self.width:
            raise IndexError("Attempt to get cell at invalid position {0},{1}", [x, y])

        return self.cells[y][x]

    def step(self):
        self.iteration += 1

        if self.rules is None:
            self.rules = rules.ConwayRules()
        self.rules.apply_to(self)

    def reset(self):
        self.iteration = 0

    def livingNeighbors(self, x, y):
        """ Deprecated """
        return self.living_neighbors(x, y)

    def living_neighbors(self, x, y):
        neighbors = [
            self.neighborAt(self.f_filter_above(x, y), self.f_at_above(x, y)),
            self.neighborAt(self.f_filter_below(x, y), self.f_at_below(x, y)),
            self.neighborAt(self.f_filter_left(x, y), self.f_at_left(x, y)),
            self.neighborAt(self.f_filter_right(x, y), self.f_at_right(x, y)),
            self.neighborAt(self.f_filter_UL(x, y), self.f_at_UL(x, y)),
            self.neighborAt(self.f_filter_UR(x, y), self.f_at_UR(x, y)),
            self.neighborAt(self.f_filter_LL(x, y), self.f_at_LL(x, y)),
            self.neighborAt(self.f_filter_LR(x, y), self.f_at_LR(x, y)),
        ]
        return sum([1 for neighbor in neighbors if neighbor == cell.Alive])

    def f_filter_above(self, x, y):
        return lambda: y == 0

    def f_at_above(self, x, y): 
        return lambda: self.cellAt(x, y-1)

    def f_filter_below(self, x, y):
        return lambda: y == self.height-1

    def f_at_below(self, x, y): 
        return lambda: self.cellAt(x, y+1)

    def f_filter_left(self, x, y):
        return lambda: x == 0

    def f_at_left(self, x, y): 
        return lambda: self.cellAt(x-1, y)

    def f_filter_right(self, x, y):
        return lambda: x == self.width-1

    def f_at_right(self, x, y): 
        return lambda: self.cellAt(x+1, y)

    def f_filter_UL(self, x, y):
        return lambda: x == 0 or y == 0

    def f_at_UL(self, x, y): 
        return lambda: self.cellAt(x-1, y-1)

    def f_filter_UR(self, x, y):
        return lambda: x == self.width-1 or y == 0

    def f_at_UR(self, x, y): 
        return lambda: self.cellAt(x+1, y-1)

    def f_filter_LL(self, x, y):
        return lambda: x == 0 or y == self.height-1

    def f_at_LL(self, x, y): 
        return lambda: self.cellAt(x-1, y+1)

    def f_filter_LR(self, x, y):
        return lambda: x == self.width-1 or y == self.height-1

    def f_at_LR(self, x, y): 
        return lambda: self.cellAt(x+1, y+1)

    def neighborAt(self, f_filter, f_at):
        if f_filter():
            return cell.Dead
        return f_at().mortality

    def map_rows(self, f):
        return [f(y) for y in range(self.height)]

    def map_columns(self, f):
        return [f(x) for x in range(self.width)]

    def map(self, f):
        return self.map_rows(lambda y: self.map_columns(lambda x: f(x, y, self.cell_at(x, y))))

    def for_each(self, f):
        self.map(f)
