#
# @lc app=leetcode.cn id=2397 lang=python3
# @lcpr version=30204
#
# [2397] 被列覆盖的最多行数
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        row = len(matrix)
        col = len(matrix[0])

        # C(col, numselect)

        path = []
        res = 0

        def numCovered(selectedCols):
            res = 0
            for r in range(row):
                res += 1
                for c in range(col):
                    if matrix[r][c] == 1 and c not in selectedCols:
                        res -= 1
                        break
            return res
                

        def backtrack(start):
            nonlocal res

            if len(path) == numSelect:
                num = numCovered(set(path))
                res = max(res, num)
                return

            for i in range(start, col):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res
# @lc code=end



#
# @lcpr case=start
# [[0,0,0],[1,0,1],[0,1,1],[0,0,1]]\n2\n
# @lcpr case=end

# @lcpr case=start
# [[1],[0]]\n1\n
# @lcpr case=end

#

