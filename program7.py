import heapq
from typing import List, Tuple

class ShortestPath:
    """Class to compute shortest paths in an edge-weighted directed graph."""

    def __init__(self, vertices: int):
        self.V = vertices

        # Adjacency list for Dijkstra
        self.adj: List[List[Tuple[int, int]]] = [[] for _ in range(vertices)]

        # Edge list for Bellman-Ford
        self.edges: List[Tuple[int, int, int]] = []

    def add_edge(self, u: int, v: int, weight: int):
        """Adds a directed edge from u to v with a given weight."""
        self.adj[u].append((v, weight))
        self.edges.append((u, v, weight))

    def dijkstra(self, src: int) -> List[int]:
        """
        Dijkstra's algorithm for finding single-source shortest paths.
        Does not work with negative edge weights.
        """

        dist = [float('inf')] * self.V
        dist[src] = 0

        pq = [(0, src)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            if current_dist > dist[u]:
                continue

            for v, weight in self.adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        return [int(d) if d != float('inf') else -1 for d in dist]

    def bellman_ford(self, src: int) -> List[int]:
        """
        Bellman-Ford algorithm for finding single-source shortest paths.
        Works with negative edge weights and detects negative weight cycles.
        """

        dist = [float('inf')] * self.V
        dist[src] = 0

        # Relax all edges V-1 times
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Check for negative-weight cycles
        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                raise ValueError("Graph contains a negative-weight cycle.")

        return [int(d) if d != float('inf') else -1 for d in dist]


# Example Usage
if __name__ == "__main__":

    # Create a graph with 6 vertices
    sp = ShortestPath(6)

    # Add directed edges
    sp.add_edge(0, 1, 4)
    sp.add_edge(0, 2, 8)
    sp.add_edge(1, 2, 2)
    sp.add_edge(1, 3, 5)
    sp.add_edge(2, 3, 1)
    sp.add_edge(2, 4, 7)
    sp.add_edge(3, 4, 3)
    sp.add_edge(3, 5, 6)
    sp.add_edge(4, 5, 2)

    print("Dijkstra Distances from source 0:")
    print(sp.dijkstra(0))

    print("\nBellman-Ford Distances from source 0:")
    print(sp.bellman_ford(0))

    # Example with a negative cycle
    sp_neg = ShortestPath(3)

    sp_neg.add_edge(0, 1, 2)
    sp_neg.add_edge(1, 2, -4)
    sp_neg.add_edge(2, 0, 1)

    try:
        print("\nAttempting Bellman-Ford on graph with negative cycle:")
        sp_neg.bellman_ford(0)

    except ValueError as e:
        print(f"Error caught: {e}")
