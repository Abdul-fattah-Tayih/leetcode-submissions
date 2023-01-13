from typing import List


class ValidSudoku:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_uniqueness = [set() for row in board]
        column_uniqueness = [set() for col in board[0]]
        box_uniqueness = [set() for row in board]

        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                # skip empty cells
                if col == '.':
                    continue

                if col in row_uniqueness[row_index]:
                    return False

                row_uniqueness[row_index].add(col)

                if col in column_uniqueness[col_index]:
                    return False

                column_uniqueness[col_index].add(col)

                box_index = self.get_box_index(row_index, col_index)
                if col in box_uniqueness[box_index]:
                    return False

                box_uniqueness[box_index].add(col)

        return True

    def get_box_index(self, row, col) -> int:
        boxes = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]

        box_row = boxes[int(((row + 1) / 3) + ((row + 1) % 3))]

        return box_row[int(((col + 1) / 3) + ((col + 1) % 3))]


if __name__ == '__main__':
    obj = ValidSudoku()

    assert obj.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
                             "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) == True

    assert obj.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
                             "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) == False
