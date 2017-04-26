Alive = "Alive"
Dead = "Dead"

class Cell(object):
    mortality = None

class LiveCell(Cell):
    mortality = Alive

class DeadCell(Cell):
    mortality = Dead
