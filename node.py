class Node:
    def __init__(self, value: str):
        self.value = value
        self.connections = dict()

    def __str__(self) -> str:
        return self.value

    def connect_node(self, node):
        assert isinstance(node, Node)
        self.connections[node.value] = node
