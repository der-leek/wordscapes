from board import Board
from solver import Solver


def main():
    letters = input("Enter your board: ")
    board = Board(letters)
    solver = Solver(board, set())
    solver.solve_board()
    print(solver.words)


if __name__ == "__main__":
    main()
