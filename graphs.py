import string
from searching import *


class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.nodes = [i for i in string.ascii_lowercase[:len(self.matrix[0])]]

    def connected_to(self, node):  # Return node connected to arg node
        index = linear_search(list(string.ascii_lowercase), node)
        if type(index) == int:
            return [v for i, v in enumerate(string.ascii_lowercase[:len(self.matrix[0])]) if self.matrix[index][i] != 0]
        else:
            return 'Node not in graph'


# An adjacency matrix for a graph where node 1 is connected to
# nodes 2, 3 and 4
ad_mat = [[0, 1, 1, 1],
          [1, 0, 0, 0],
          [1, 0, 0, 0],
          [1, 0, 0, 0]]

G = Graph(ad_mat)

print(G.connected_to('a'))
