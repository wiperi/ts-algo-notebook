#
# @lc app=leetcode.cn id=79 lang=python3
# @lcpr version=30204
#
# [79] 单词搜索
#


# @lcpr-template-start
from turtle import back
from typing import List, Optional

from httpcore import ConnectionInterface
import rpds
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        row = len(board)
        col = len(board[0])

        res = False

        def backtrack(r, c, ind):
            nonlocal res

            if res is True:
                return

            if ind == len(word) - 1:
                res = True
                return

            for dr, dc in directions:
                rr = r + dr
                cc = c + dc

                if not (0 <= rr < row) or not (0 <= cc < col):
                    continue

                if board[rr][cc] != word[ind + 1]:
                    continue

                if vis[rr][cc]:
                    continue

                vis[rr][cc] = True
                backtrack(rr, cc, ind + 1)
                vis[rr][cc] = False

        for r in range(row):
            for c in range(col):
                if board[r][c] == word[0]:
                    vis = [[False] * col for _ in range(row)]
                    vis[r][c] = True
                    backtrack(r, c, 0)
        
        return res


# @lc code=end


#
# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"SEE"\n
# @lcpr case=end

# @lcpr case=start
# [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCB"\n
# @lcpr case=end

#
