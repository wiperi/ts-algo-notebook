#
# @lc app=leetcode.cn id=73 lang=python3
# @lcpr version=30204
#
# [73] 矩阵置零
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
        # Check if first row and first column need to be zeroed
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(col))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(row))
        
        # Use first row and first column as markers
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
        
        # Set zeros based on markers (except first row and column)
        for r in range(1, row):
            if matrix[r][0] == 0:
                for c in range(1, col):
                    matrix[r][c] = 0
        
        for c in range(1, col):
            if matrix[0][c] == 0:
                for r in range(1, row):
                    matrix[r][c] = 0
        
        # Set first row and column to zero if needed
        if first_row_has_zero:
            for c in range(col):
                matrix[0][c] = 0
                
        if first_col_has_zero:
            for r in range(row):
                matrix[r][0] = 0


# @lc code=end


#
# @lcpr case=start
# [[1,1,1],[1,0,1],[1,1,1]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]\n
# @lcpr case=end

#
