from typing import List, Deque
from collections import deque

class NumberOfIslands:
    """
        200. Number of Islands

        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 

        You may assume all four edges of the grid are all surrounded by water.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        """
            Breadth first search

            O(n^2*v+e)

            # define a queue for traversal
            # define a set for visited nodes

            # loop over rows and cols
                # continue if row,col is in visited
                # if element == 1 add it to queue
                
                # if queue is not empty
                    # while queue is not empty:
                        # check all four directions, if any of them contains a '1' add them to the queue and visited
                        
                    # increment island count by 1
                    
            # return island count

            Explanation: 
            
            Whenever we find a '1', we try to do a BFS using it as the root node, by adding all elements that are equal to '1'

            that are adjacent vertically or horizontally, and each element we find we add it to visited nodes to avoid circular infinite loops

            https://leetcode.com/problems/number-of-islands/submissions/868721672/
        """
        queue = deque() # type: Deque[str]
        visited = set()
        island_count = 0
        
        for row_index, row in enumerate(grid):
            for col_index, col in enumerate(row):
                if f'{row_index},{col_index}' in visited:
                    continue
                    
                if col == '1':
                    queue.append(f'{row_index},{col_index}')
                    visited.add(f'{row_index},{col_index}')
                    
                if queue:
                    while queue:
                        traversal_row, traversal_col = map(int, queue.popleft().split(','))
                        if traversal_row + 1 < len(grid) and grid[traversal_row+1][traversal_col] == '1' and f'{traversal_row+1},{traversal_col}' not in visited:
                            queue.append(f'{traversal_row+1},{traversal_col}')
                            visited.add(f'{traversal_row+1},{traversal_col}')

                        if traversal_row - 1 >= 0 and grid[traversal_row-1][traversal_col] == '1' and f'{traversal_row-1},{traversal_col}' not in visited:
                            queue.append(f'{traversal_row-1},{traversal_col}')
                            visited.add(f'{traversal_row-1},{traversal_col}')

                        if traversal_col - 1 >= 0 and grid[traversal_row][traversal_col-1] == '1' and f'{traversal_row},{traversal_col-1}' not in visited:
                            queue.append(f'{traversal_row},{traversal_col-1}')
                            visited.add(f'{traversal_row},{traversal_col-1}')

                        if traversal_col + 1 < len(row) and grid[traversal_row][traversal_col+1] == '1' and f'{traversal_row},{traversal_col+1}' not in visited:
                            queue.append(f'{traversal_row},{traversal_col+1}')
                            visited.add(f'{traversal_row},{traversal_col+1}')
                    
                    island_count += 1
                    
        return island_count

if __name__ == '__main__':
    obj = NumberOfIslands()

    assert obj.numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]) == 1

    assert obj.numIslands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]) == 3