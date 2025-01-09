import logging
from trie import Trie
from node import Node
from board import Board
from time import perf_counter


class Solver:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filemode="w",
        filename="solver.log",
    )

    def __init__(self, board: Board, words: set):
        self.words = words
        self.board = board
        self.dictionary: Trie = Trie.load("dictionary.trie")
        self.positions_searched = 0

    def solve_board(self):
        start = perf_counter()

        for letter in self.board.board:
            self.__find_words(letter, "", [])

        finish = perf_counter()
        elapsed_time = round(finish - start, 3)
        self.__log_results(elapsed_time)

    def __find_words(self, node: Node, word: str, path: list):
        self.positions_searched += 1

        if node in path or not self.dictionary.contains(word):
            return

        path.append(node)
        word += node.value

        if self.dictionary.is_word(word):
            self.words.add(word)

        for connection in node.connections:
            self.__find_words(connection, word, path)

        path.pop()

    def __log_results(self, elapsed_time):
        logging.debug(
            f"Searched {self.positions_searched} positions in {elapsed_time} seconds"
        )
        logging.debug(f"Found {len(self.words)} solutions")
