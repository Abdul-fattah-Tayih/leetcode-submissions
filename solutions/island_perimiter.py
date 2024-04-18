from collections import deque
import copy
from typing import List

class IslandPerimiter:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        start = (0, 0)
        found = False
        for i in range(len(grid)):
            if found:
                break

            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    start = (i, j)
                    found = True

                if found:
                    break

        crack = copy.deepcopy(grid)

        q = deque([start])
        visited = set()
        result = 0
        
        while q:
            length = len(q)
            for _ in range(length):
                row, col = q.popleft()

                if (row, col) in visited:
                        continue

                visited.add((row, col))

                block_perimeter = 4

                for row_addition, col_addition in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_row = row + row_addition
                    next_col = col + col_addition

                    if next_row < 0 or next_row >= len(grid):
                        continue

                    if next_col < 0 or next_col >= len(grid[0]):
                        continue

                    if grid[next_row][next_col] != 1:
                        continue
                    
                    block_perimeter -= 1

                    if (next_row, next_col) in visited:
                        continue

                    q.append((next_row, next_col))

                result += block_perimeter

        return result

if __name__ == '__main__':
    obj = IslandPerimiter()
    print(obj.islandPerimeter([[1,1],[1,1]]))