#
# @lc app=leetcode.cn id=51 lang=python3
# @lcpr version=30104
#
# [51] N 皇后
#

# @lc code=start


from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0 for _ in range(n)] for _ in range(n)]
        res = []

        def valid(board, row, col):
            for i in range(row):
                if board[i][col] == 1:
                    return False

            for r, c in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
                if board[r][c] == 1:
                    return False

            for r, c in zip(range(row - 1, -1, -1), range(col + 1, n, 1)):
                if board[r][c] == 1:
                    return False

            return True

        def backtrack(board: list[list[int]], row: int):
            if row == n:
                solution = []
                for r in board:
                    solution.append("".join("Q" if num == 1 else "." for num in r))
                res.append(solution)
                return

            for c in range(n):
                if not valid(board, row, c):
                    continue
                board[row][c] = 1
                backtrack(board, row + 1)
                board[row][c] = 0

        backtrack(board, 0)
        return res


# @lc code=end


#
# @lcpr case=start
# 4\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#
