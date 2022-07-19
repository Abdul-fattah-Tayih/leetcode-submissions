from typing import List

class FloodFill:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int):
        old_color = image[sr][sc]
        # check if old_color is already painted
        if old_color != color:            
            self.dfs(image, sr, sc, old_color, color)
        return image

    def dfs(self, image, r, c, color, new_color):
        # base step
        if r < 0 or r >= len(image) or \
           c < 0 or c >= len(image[r]) or \
           image[r][c] != color:
           return 

        # fill current node
        image[r][c] = new_color
        
        # recursive step
        self.dfs(image, r+1, c, color, new_color)
        self.dfs(image, r-1, c, color, new_color)
        self.dfs(image, r, c+1, color, new_color)
        self.dfs(image, r, c-1, color, new_color)

        
if __name__ == '__main__':
    solution = FloodFill()
    print(solution.floodFill(
        [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1],
        ], 
        1, 
        1, 
        2
    ))

    print(
        solution.floodFill(
            [
                [0,0,0],
                [1,0,0]
            ],
            1,
            1,
            2
        )
    )