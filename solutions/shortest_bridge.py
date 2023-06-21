from collections import deque
from typing import List, Set

class ShortestBridge:
    """
        934. Shortest Bridge

        You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

        An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

        You may change 0's to 1's to connect the two islands to form one island.

        Return the smallest number of 0's you must flip to connect the two islands.

        
        Example 1:
        Input: grid = [[0,1],[1,0]]
        Output: 1
        
        Example 2:
        Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
        Output: 2

        Example 3:
        Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
        Output: 1

        Constraints:
        1. n == grid.length == grid[i].length
        2. 2 <= n <= 100
        3. grid[i][j] is either 0 or 1.
        4. There are exactly two islands in grid.
    """
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # find island coordinates
            # dfs/bfs when you encounter the first 1

        # bfs through each point in island1 to find paths to island 2
            # only move towards water

            # if any adjacent point is either visited before or is part of island 1, then ignore it

            # stop if you find a coordinate that is land (= 1) and is not part of island1

        # return shortest path

        """
            O(n^2) solution

            # find island coordinates
                # dfs/bfs when you encounter the first 1 to find all the coordinates for the first island

            # bfs through each point in island1 to find paths to island 2
                # only move towards water

                # if any adjacent point is either visited before or is part of island 1, then ignore it

                # stop if you find a coordinate that is land (= 1) and is not part of island1

            # return shortest path
        """

        island1 = self.find_first_island(grid)
        min_length = len(grid) ** 2

        for row, col in island1:
            visited = island1.copy()
            q = deque([(row, col, 0)]) # we store row, col and the distance

            while q:
                size = len(q)
                for _ in range(size):
                    next_row, next_col, length = q.popleft()
                    if (next_row, next_col) not in island1 and grid[next_row][next_col] == 1:
                        min_length = min(min_length, length - 1)

                    for coordinates in self.get_valid_four_directional_indices(next_row, next_col, grid, visited, False):
                        q.append((coordinates[0], coordinates[1], length + 1))
                        visited.add(coordinates)
        
        return min_length

    def get_valid_four_directional_indices(self, row, col, grid, visited, equals_one = True):
        valid_indices = []
        for row, col in [(row, col + 1), (row, col - 1), (row + 1, col), (row - 1, col)]:
            if (
                row >= 0 and row < len(grid)
                and col >= 0 and col < len(grid) 
                and (equals_one == False or (equals_one == True and grid[row][col] == 1))
                and (row, col) not in visited
            ):

                valid_indices.append((row, col))

        return valid_indices
    
    def find_first_island(self, grid):
        island1 = set()
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if col == 0 or (row_index, col_index) in island1:
                    continue

                q = deque([(row_index, col_index)])
                island1.add((row_index, col_index))
                while q:
                    size = len(q)
                    for _ in range(size):
                        next_row, next_col = q.popleft()
                        for coordinates in self.get_valid_four_directional_indices(next_row, next_col, grid, island1):
                            q.append(coordinates)
                            island1.add(coordinates)

                return island1
        
        return island1
    
obj = Solution()
print(obj.shortestBridge([[0,1,0],[0,0,0],[0,0,1]]))
print(obj.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]))