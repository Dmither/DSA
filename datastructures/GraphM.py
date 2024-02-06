class Graph:
    def __init__(self, size, directed=False, weighted=False, looped=False):
        self.adjMatrix = []
        self.directed = directed
        self.weighted = weighted
        self.looped = looped
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size
    def add_edge(self, v1, v2, weidht=1):
        if v1 < 0 or v2 < 0:
            raise Exception("Graph does not contain negative values")
        try:
            if self.adjMatrix[v1][v2] == 1:
                raise Exception(f"Already contains edge between {v1} and {v2}")
            if not self.looped:
                if v1 == v2:
                    raise Exception(f"Same vertex {v1}. Graph cannot have loops")
            self.adjMatrix[v1][v2] = weidht if self.weighted else 1
            if not self.directed:
                self.adjMatrix[v2][v1] = weidht if self.weighted else 1
            return self
        except IndexError:
            raise Exception(f"Graph does not contain {v1} or {v2}")
    def remove_edge(self, v1, v2):
        if v1 < 0 or v2 < 0:
            raise Exception("Graph does not contain negative values")
        try:
            if self.adjMatrix[v1][v2] == 0:
                raise Exception(f"No edge between {v1} and {v2}")
            self.adjMatrix[v1][v2] = 0
            if not self.directed:
                self.adjMatrix[v2][v1] = 0
            return self
        except IndexError:
            raise Exception(f"Graph does not contain {v1} or {v2}")
    def __len__(self):
        return self.size
    def print_matrix(self):
        print("#|", end="")
        for i in range(self.size):
            print(f" {i}", end="")
        print()
        print("-" + "+" + "--" * self.size)
        for i in range(self.size):
            print(f"{i}|", end="")
            for j in range(self.size):
                print(f" {self.adjMatrix[i][j]}", end="")
            print()
        print()

graph = Graph(3, False, False, True)
graph.print_matrix()
graph.add_edge(0, 1, 2)
graph.print_matrix()
graph.add_edge(0, 2, 3)
graph.print_matrix()
graph.add_edge(1, 2, 4)
graph.print_matrix()
graph.add_edge(0, 0, 1)
graph.print_matrix()


# Список суміжності:
# graph = {
#     "A": {"B", "C"},
#     "B": {"A", "D", "E"},
#     "C": {"A", "F"},
#     "D": {"B"},
#     "E": {"B", "F"},
#     "F": {"C", "E"},
# }