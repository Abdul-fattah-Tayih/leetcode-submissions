from typing import List

class Search2dMatrix:
    """
        74. Search a 2D Matrix

        Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

        Integers in each row are sorted from left to right.

        The first integer of each row is greater than the last integer of the previous row.
    """
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
            O(m log(n))

            The idea is that we binary search each row, which cuts complexity from o(n^2) to O(m log(n))

            https://leetcode.com/problems/search-a-2d-matrix/submissions/855811816/
        """

        for row in matrix:
            if self.binary_search(row, target):
                return True

        return False

    def binary_search(self, row: List[int], target: int) -> bool:
        left = 0
        right = len(row) - 1

        while left <= right:
            mid = int(left + (right - left) / 2)
            if row[mid] == target:
                return True

            if row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
