"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example:
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
"""

class Graph:

    def __init__(self, edge_matrix):
        self.edge_matrix = edge_matrix
        self.num_nodes = len(edge_matrix)
        self.parent = [i for i in range(self.num_nodes)]
        self.rank = [1] * self.num_nodes

    def find(self, node):
        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.parent[self.parent[node]]
            return self.find(self.parent[node])

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return 0
        else:
            if self.rank[node1] > self.rank[node2]:
                self.parent[parent2] = parent1
                self.rank[parent1] = self.rank[parent1] + self.rank[parent2]
            else:
                self.parent[parent1] = parent2
                self.rank[parent2] = self.rank[parent2] + self.rank[parent1]
            return 1

    def get_num_provinces(self):
        num_nodes = len(self.edge_matrix)
        num_connected_components = self.num_nodes
        for i in range(self.num_nodes - 1):
            for j in range(i, self.num_nodes):
                if j == i:
                    continue
                if self.edge_matrix[i][j]:
                    num_connected_components = num_connected_components - self.union(i, j)

        return num_connected_components


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        return Graph(isConnected).get_num_provinces()


if __name__ == "__main__":
    s = Solution()
    assert (s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2)
    assert (s.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3)
