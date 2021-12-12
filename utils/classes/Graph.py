class Node:

    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
        self.nodes = []

    def __repr__(self):
        result = ""
        for node in self.nodes:
            result += f"{self.name} <-> {node.name}\n"

        return result

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_child(self, child):
        self.children.append(child)

    def add_node(self, node):
        self.nodes.append(node)


class Graph:

    def __init__(self, nodes):
        self.nodes = nodes

    def get_node(self, node_name):
        return self.nodes.get(node_name, None)
