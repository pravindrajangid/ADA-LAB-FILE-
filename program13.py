from typing import List

class TSPSolver:
    """
    Class to solve the Traveling Salesperson Problem (TSP).
    Finds the minimum cost to visit all nodes exactly once and return to the starting node.
    """

    def solve_tsp(self, dist_matrix: List[List[int]]) -> int:
        """
        Calculates the minimum tour cost using Dynamic Programming and Bitmasking (Held-Karp algorithm).
        """

        n = len(dist_matrix)

        if n == 0:
            return 0

        if n == 1:
            return dist_matrix[0][0]

        # ALL_VISITED is a bitmask where all 'n' bits are set to 1.
        ALL_VISITED = (1 << n) - 1

        # Memoization table
        memo = {}

        def tsp(mask: int, pos: int) -> int:
            """
            Recursive helper function to find the minimum cost path.
            """

            # Base case: Return to starting city
            if mask == ALL_VISITED:
                return dist_matrix[pos][0]

            # Check if state is already computed
            if (mask, pos) in memo:
                return memo[(mask, pos)]

            min_cost = float('inf')

            # Try visiting every other city
            for city in range(n):

                # Check if the city is unvisited
                if (mask & (1 << city)) == 0:

                    # Mark the new city as visited
                    new_mask = mask | (1 << city)

                    # Calculate cost and recurse
                    cost = dist_matrix[pos][city] + tsp(new_mask, city)

                    min_cost = min(min_cost, cost)

            # Store the computed minimum cost
            memo[(mask, pos)] = min_cost

            return min_cost

        # Start the tour at city 0
        return tsp(1, 0)


# Example Usage
if __name__ == "__main__":

    # Example adjacency matrix representing distances between 5 cities
    distance_matrix = [
        [0, 12, 18, 25, 30],
        [12, 0, 20, 15, 22],
        [18, 20, 0, 28, 16],
        [25, 15, 28, 0, 14],
        [30, 22, 16, 14, 0]
    ]

    solver = TSPSolver()

    min_tour_cost = solver.solve_tsp(distance_matrix)

    print("Distance Matrix:")

    for row in distance_matrix:
        print(row)

    print(f"\nMinimum TSP Tour Cost: {min_tour_cost}")
