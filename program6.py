
from typing import List, Tuple
import heapq


# Edge format: (weight, source, destination)
Edge = Tuple[int, int, int]


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges: List[Edge] = []
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int, weight: int):
        # Store edge for Kruskal's algorithm
        self.edges.append((weight, u, v))

        # Store edge in adjacency list for Prim's algorithm
        self.adj[u].append((weight, v))
        self.adj[v].append((weight, u))

    # Kruskal's Minimum Spanning Tree
    def kruskal_mst(self) -> List[Edge]:
        parent = list(range(self.vertices))
        rank = [0] * self.vertices

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

            return True

        mst = []

        for weight, u, v in sorted(self.edges):
            if union(u, v):
                mst.append((weight, u, v))

            if len(mst) == self.vertices - 1:
                break

        return mst

    # Prim's Minimum Spanning Tree
    def prim_mst(self) -> List[Edge]:
        if self.vertices == 0:
            return []

        visited = [False] * self.vertices
        mst = []

        visited[0] = True
        heap = []

        for weight, v in self.adj[0]:
            heapq.heappush(heap, (weight, 0, v))

        while heap and len(mst) < self.vertices - 1:
            weight, u, v = heapq.heappop(heap)

            if visited[v]:
                continue

            visited[v] = True
            mst.append((weight, u, v))

            for next_weight, next_vertex in self.adj[v]:
                if not visited[next_vertex]:
                    heapq.heappush(
                        heap, (next_weight, v, next_vertex)
                    )

        return mst


# Main Program
if __name__ == "__main__":
    vertices = 5
    graph = Graph(vertices)

    # Add edges: source, destination, weight
    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, 5)
    graph.add_edge(2, 4, 7)
    graph.add_edge(3, 4, 9)

    # Kruskal's MST
    print("Kruskal's Minimum Spanning Tree:")
    kruskal_result = graph.kruskal_mst()

    for weight, u, v in kruskal_result:
        print(f"{u} -- {v} : Weight = {weight}")

    print("Total MST Weight =", sum(e[0] for e in kruskal_result))

    # Prim's MST
    print("\nPrim's Minimum Spanning Tree:")
    prim_result = graph.prim_mst()

    for weight, u, v in prim_result:
        print(f"{u} -- {v} : Weight = {weight}")

    print("Total MST Weight =", sum(e[0] for e in prim_result))
