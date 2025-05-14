#
# @lc app=leetcode.cn id=304 lang=python3
# @lcpr version=30204
#
# [304] 二维区域和检索 - 矩阵不可变
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.preSum = [[0] * (col + 1) for _ in range(row + 1)]

        for r in range(1, row + 1):
            s = 0
            for c in range(1, col + 1):
                s += matrix[r - 1][c - 1]
                self.preSum[r][c] = self.preSum[r - 1][c] + s

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.preSum
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        return (
            s[row2][col2]
            - (s[row2][col1 - 1] + s[row1 - 1][col2])
            + s[row1 - 1][col1 - 1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end


#
# @lcpr case=start
# ["NumMatrix","sumRegion","sumRegion","sumRegion"][[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]\n
# @lcpr case=end

#
