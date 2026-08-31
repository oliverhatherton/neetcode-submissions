class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for row_index, row in enumerate(board):
            for col_index, cell in enumerate(row):
                if cell == ".":
                    continue

                box_index = (row_index // 3) * 3 + (col_index // 3)

                if cell in rows[row_index] or cell in cols[col_index] or cell in boxs[box_index]:
                    return False

                rows[row_index].add(cell)
                cols[col_index].add(cell)
                boxs[box_index].add(cell)

        return True