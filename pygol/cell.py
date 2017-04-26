Alive = "Alive"
Dead = "Dead"

class Cell(object):
    mortality = None

    def is_alive(self):
        return self.mortality == Alive

    def is_dead(self):
        return self.mortality == Dead

class LiveCell(Cell):
    mortality = Alive

class DeadCell(Cell):
    mortality = Dead
