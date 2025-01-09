class Node:
    def __init__(self, value: str):
        self.value = value
        self.connections = []

    def __str__(self) -> str:
        return f"{self.value}: {[node.value for node in self.connections]}"

    def connect_to_node(self, node):
        assert isinstance(node, Node)
        self.connections.append(node)
