#
# @lc app=leetcode.cn id=51 lang=python3
# @lcpr version=30204
#
# [51] N 皇后
#


# @lcpr-template-start
from copy import deepcopy
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [[0] * n for _ in range(n)]
        res = []

        def valid(r, c):
            for i in range(n):
                if r - i >= 0 and board[r - i][c] == 1:
                    return False
                if r - i >= 0 and c - i >= 0 and board[r - i][c - i] == 1:
                    return False
                if r - i >= 0 and c + i < n and board[r - i][c + i] == 1:
                    return False

            return True

        def backtrack(row):
            if row == n:
                result = []
                for arr in board:
                    row_str = ''
                    for cell in arr:
                        if cell == 1:
                            row_str += 'Q'
                        else:
                            row_str += '.'
                    result.append(row_str)
                res.append(result)
                return

            for col in range(n):
                if not valid(row, col):
                    continue

                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

        backtrack(0)

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
