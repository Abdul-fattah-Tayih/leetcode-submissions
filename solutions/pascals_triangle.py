from typing import List
import unittest


class PascalsTriangle:
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

if __name__ == '__main__':
    test = unittest.main('tests.test_pascals_triangle', exit=False)