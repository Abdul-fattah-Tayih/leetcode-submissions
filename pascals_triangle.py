from typing import List
from colorama import Fore

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row in range(numRows):
            element_count = row + 1
            triangle_row = []
            for col in range(element_count):
                triangle_row.append(self.__get_cell_value(triangle, row, col))
            
            triangle.append(triangle_row)

        return triangle

    def __get_cell_value(self, triangle, row, column):
        if column == 0 or column == row: return 1

        return triangle[row - 1][column] + triangle[row - 1][column - 1]

solution = Solution()

cases = {
    5: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]],
    4: [[1],[1,1],[1,2,1],[1,3,3,1]],
    1: [[1]],
}

for case, expected_result in cases.items():
    actual_result = solution.generate(case)
    if (actual_result != expected_result):
        print(f'{Fore.RED} x failed test, input: {case}')
    else:
        print(f'{Fore.GREEN} passed!')