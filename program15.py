from typing import List

class GraphBacktracker:
    """
    A class to solve graph-related problems using backtracking,
    specifically Graph Coloring and Hamiltonian Cycle.
    """

    def __init__(self, graph: List[List[int]]):
        self.graph = graph
        self.V = len(graph)

    def graph_coloring(self, m: int) -> List[int]:
        colors = [0] * self.V

        def is_safe(v: int, c: int) -> bool:
            for i in range(self.V):
                if self.graph[v][i] == 1 and colors[i] == c:
                    return False
            return True

        def backtrack(v: int) -> bool:
            if v == self.V:
                return True

            for c in range(1, m + 1):
                if is_safe(v, c):
                    colors[v] = c

                    if backtrack(v + 1):
                        return True

                    colors[v] = 0

            return False

        if backtrack(0):
            return colors
        return []

    def hamiltonian_cycle(self) -> List[int]:
        path = [-1] * self.V

        def is_safe(v: int, pos: int) -> bool:
            if self.graph[path[pos - 1]][v] == 0:
                return False

            if v in path:
                return False

            return True

        def backtrack(pos: int) -> bool:
            if pos == self.V:
                if self.graph[path[pos - 1]][path[0]] == 1:
                    return True
                return False

            for v in range(1, self.V):
                if is_safe(v, pos):
                    path[pos] = v

                    if backtrack(pos + 1):
                        return True

                    path[pos] = -1

            return False

        path[0] = 0

        if backtrack(1):
            return path + [path[0]]

        return []


# Example Usage:
if __name__ == "__main__":

    # Updated Example Adjacency Matrix
    graph_matrix = [
        [0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0]
    ]

    backtracker = GraphBacktracker(graph_matrix)

    # 1. Graph Coloring Example
    num_colors = 3
    color_mapping = backtracker.graph_coloring(num_colors)

    print(f"Graph Coloring (Max {num_colors} colors):")

    if color_mapping:
        print(f"Vertex color mapping: {color_mapping}")
    else:
        print("No valid coloring exists.")

    print("\n" + "-" * 30 + "\n")

    # 2. Hamiltonian Cycle Example
    cycle_path = backtracker.hamiltonian_cycle()

    print("Hamiltonian Cycle:")

    if cycle_path:
        print(f"Valid cycle path: {'-> '.join(map(str, cycle_path))}")
    else:
        print("No Hamiltonian Cycle exists.")