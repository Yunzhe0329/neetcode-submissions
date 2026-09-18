class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROW = defaultdict(set)
        COL = defaultdict(set)
        sub_boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in ROW[r] or board[r][c] in COL[c] or board[r][c] in sub_boxes[(r // 3, c // 3)]:
                    return False
                ROW[r].add(board[r][c])
                COL[c].add(board[r][c])
                sub_boxes[(r // 3, c // 3)].add(board[r][c])
        return True