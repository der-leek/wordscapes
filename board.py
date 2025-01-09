from node import Node


class Board:
    def __init__(self, letters: str):
        self.board = [Node(letter.upper()) for letter in letters]
        self.__connect_nodes()

    def __str__(self) -> str:
        return "".join([node.value for node in self.board])

    def __connect_nodes(self): ...