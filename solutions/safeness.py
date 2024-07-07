from typing import List


class Safeness:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        thieves = []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    thieves.append((i, j))

        def dfs(i, j, max_safeness, visited):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid):
                return max_safeness

            if (i, j) in visited:
                return 0

            if grid[i][j] == 1:
                return 0

            safeness = 1000
            for x, y in thieves:
                safeness = min(safeness, abs(i - x) + abs(j - y))

            max_safeness = max(max_safeness, safeness)

            visited.add((i, j))

            max_safeness = max(
                max_safeness,
                dfs(i, j + 1, max_safeness, visited),
                dfs(i, j - 1, max_safeness, visited),
                dfs(i + 1, j, max_safeness, visited),
                dfs(i - 1, j, max_safeness, visited)
            )

            visited.remove((i, j))

            return max_safeness

        return dfs(0, 0, 0, set())
    
if __name__ == '__main__':
    obj = Safeness()
    obj.maximumSafenessFactor([[0,0,1],[0,0,0],[0,0,0]])