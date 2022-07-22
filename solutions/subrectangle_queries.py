from curses.textpad import rectangle
from typing import List

class SubrectangleQueries:
    """
        Question: 
            Implement the class SubrectangleQueries which receives a rows x cols rectangle as a matrix 
            of integers in the constructor and supports two methods:
            
                1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
                    Updates all values with newValue in the subrectangle whose 
                    upper left coordinate is (row1,col1) and bottom right coordinate is (row2,col2).

                2. getValue(int row, int col)
                    Returns the current value of the coordinate (row,col) from the rectangle.

    """
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                self.rectangle[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        if row < len(self.rectangle) and col < len(self.rectangle[row]):
            return self.rectangle[row][col]
        
        return None

    @classmethod
    def solve_example(cls, operations: List[str], values: List):
        """
            Dynamically execute example input instead of doing it manually
        """
        object = SubrectangleQueries(*values[0])
        del operations[0]
        del values[0]

        for operation, value in zip(operations, values):
            method = getattr(object, operation)
            result = method(*value)

            print(f'Result of calling {operation} results in: {result}')

        print(f'Rectangle looks like this {object.rectangle}')

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)

if __name__ == '__main__':
    SubrectangleQueries.solve_example(
        ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"],
        [[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
    )

    SubrectangleQueries.solve_example(
        ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"],
        [[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
    )

    SubrectangleQueries.solve_example(
        ["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"],
        [[[[2,8],[8,8],[7,4]]],[1,0],[1,1,1,1,4],[1,0],[0,0],[2,1,2,1,9],[1,1],[1,0]]
    )

    SubrectangleQueries.solve_example(
        ["SubrectangleQueries","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"],
        [[[[3,9,4],[5,6,10]]],[1,1,1,1,5],[1,0],[1,0],[0,0,1,0,6],[1,0],[0,1]]
    )