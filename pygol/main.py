from board import Board
from cell import LiveCell
from board_format import PlaintextBoardFormat

if __name__ == '__main__':
    board = Board(3,3)
    board.set_cell_at(0, 1, LiveCell())
    board.set_cell_at(1, 1, LiveCell())
    board.set_cell_at(2, 1, LiveCell())
    print PlaintextBoardFormat(board, "Blinker").serialize()
    board.step()
    print PlaintextBoardFormat(board, "Blinker").serialize()
    board.step()
    print PlaintextBoardFormat(board, "Blinker").serialize()

