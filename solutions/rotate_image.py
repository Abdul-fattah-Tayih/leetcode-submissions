from typing import List

class RotateImage:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """       
          1 | 2 | 3 
          4 | 5 | 6 
          7 | 8 | 9

          in each iteration, we put the following:
            1. the first element of the row at the end
            2. the last element of the row at the last row
            3. the last element of the last row at the beginning of the last row
            4. the last element of the last row at the beginning of the first row

          so in the above example:
            1. put 1 at the place of 3
            2. put 3 at the place of 9
            3. put 9 at the place or 7
            4. put 7 at the place of 1

          then we iterate and put:
            1. 2 at the place of 6
            2. 6 at the place of 8
            3. 8 at the place of 4
            4. 4 at the place of 2
        """

        last_col_index = len(matrix[0]) - 1
        last_row_index = len(matrix) - 1

        for row in range(len(matrix)):
            col_start = row
            col_end = last_col_index - col_start
            row_end = last_row_index - row
            for col in range(col_start, col_end):
                # coordinates for the elements
                current_element_coordinates = (row, col)
                right_element_coordinates = (col, col_end)
                bottom_element_coordinates = (row_end, last_col_index - col)
                left_element_coordinates = (last_row_index - col, col_start)

                # get the elements at the coordinates
                current_element_to_be_replaced = matrix[current_element_coordinates[0]][current_element_coordinates[1]]
                right_element_to_be_replaced = matrix[right_element_coordinates[0]][right_element_coordinates[1]]
                bottom_element_to_be_replaced = matrix[bottom_element_coordinates[0]][bottom_element_coordinates[1]]
                left_element_to_be_replaced = matrix[left_element_coordinates[0]][left_element_coordinates[1]]
                
                # replace the elements with their rotated counterparts
                matrix[right_element_coordinates[0]][right_element_coordinates[1]] = current_element_to_be_replaced
                matrix[bottom_element_coordinates[0]][bottom_element_coordinates[1]] = right_element_to_be_replaced
                matrix[left_element_coordinates[0]][left_element_coordinates[1]] = bottom_element_to_be_replaced
                matrix[current_element_coordinates[0]][current_element_coordinates[1]] = left_element_to_be_replaced

"""
    This is used for testing purposes and not part of the solution, and it can be ignored
"""
def validate_solution(matrix, expected):
    print(
    f"""--------------------
input is:  {matrix}
should be: {expected}
correct? {matrix == expected}""")

if __name__ == '__main__':
    object = RotateImage()

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    object.rotate(matrix)
    validate_solution(matrix, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    object.rotate(matrix)
    validate_solution(matrix, [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]])

    matrix = [[1, 2, 3, 4, 5],  [6, 7, 8, 9, 10],  [11, 12, 13, 14, 15],  [16, 17, 18, 19, 20],  [21, 22, 23, 24, 25]]
    object.rotate(matrix)
    validate_solution(matrix, [[21, 16, 11, 6, 1], [22, 17, 12, 7, 2], [23, 18, 13, 8, 3], [24, 19, 14, 9, 4], [25, 20, 15, 10, 5]])