class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class GraphFunctions(object):

    def cloneGraph(self, node):
        if node == None:
            return None
        visited_nodes = {}
        return self.visit_node(node, visited_nodes)


    def visit_node(self, orig_node, visited_nodes):
        val = orig_node.val
        neighbors = orig_node.neighbors

        cloned_node = Node(val)
        visited_nodes[val] = cloned_node

        for neighbor in neighbors:
            cloned_neighbor = visited_nodes.get(neighbor.val)
            if cloned_neighbor == None:
                cloned_neighbor = self.visit_node(neighbor)
            cloned_node.neighbors.append(cloned_neighbor)

        return cloned_node


    def traverse(self, neighbors, coordinates):

        neighbors.append((coordinates[0]-1, coordinates[1]))
        ...


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
