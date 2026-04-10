from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                val = board[r][c]
                if val == ".":
                    continue

                hkey_box = (r//3)*3+(c//3)

                if val in rows[r] or val in columns[c] or val in boxes[hkey_box]:
                    return False
                
                rows[r].add(val)
                columns[c].add(val)
                boxes[hkey_box].add(val)

        return True
        