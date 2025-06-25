#
# @lc app=leetcode.cn id=240 lang=python3
# @lcpr version=30204
#
# [240] 搜索二维矩阵 II
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        i, j = 0, col - 1

        while i < row and j >= 0 and matrix[i][j] != target:
            if target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1

        if i < row and j >= 0:
            return True
        else:
            return False


# @lc code=end


#
# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5\n
# @lcpr case=end

# @lcpr case=start
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n20\n
# @lcpr case=end

#
