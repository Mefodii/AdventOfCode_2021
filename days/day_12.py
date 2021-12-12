from utils.classes.Graph import Node as NodeTemplate, Graph


class Node(NodeTemplate):

    def __init__(self, name):
        super().__init__(name)
        self.is_small_cave = name.islower()
        self.visits = 0
        self.limit = 1

    def is_locked(self):
        if self.is_small_cave:
            return self.visits >= self.limit
        return False


def init_nodes(connections):
    nodes = {}

    def get_node_or_new(name):
        if nodes.get(name, None) is None:
            nodes[name] = Node(name)
        return nodes[name]

    for connection in connections:
        start, end = connection.split("-")
        start_node = get_node_or_new(start)
        end_node = get_node_or_new(end)
        start_node.add_node(end_node)
        end_node.add_node(start_node)

    return nodes


def build_paths(start: Node, end: Node, nodes: dict):
    paths = []

    if start.name == end.name:
        return [[end.name]]

    if start.is_small_cave:
        start.visits += 1

    for connection in start.nodes:
        if not connection.is_locked():
            [paths.append([start.name] + path)for path in build_paths(connection, end, nodes)]

    if start.is_small_cave:
        start.visits -= 1

    return paths


def find_all_paths(nodes):
    start = nodes["start"]
    end = nodes["end"]

    paths = build_paths(start, end, nodes)
    return paths


def find_all_paths_b(nodes: dict):
    paths = set()
    for node in nodes.values():
        if node.is_small_cave and not node.name == "start":
            node.limit = 2
            for path in find_all_paths(nodes):
                paths.add(tuple(path))
            node.limit = 1

    return paths


###############################################################################
def run_a(input_data):
    nodes = init_nodes(input_data)
    paths = find_all_paths(nodes)
    result = len(paths)
    return result


def run_b(input_data):
    nodes = init_nodes(input_data)
    paths = find_all_paths_b(nodes)
    result = len(paths)
    return result
