#
# @lc app=leetcode.cn id=54 lang=python3
# @lcpr version=30204
#
# [54] 螺旋矩阵
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        row = len(matrix)
        col = len(matrix[0])

        up, left, right, bottom = 0, 0, col - 1, row - 1

        i = 0
        res = []
        while i < row * col:
            if i < row* col and left <= right:
                for c in range(left, right + 1):
                    val = matrix[up][c]
                    res.append(val)
                    i += 1
                up += 1
            
            if i < row* col and up <= bottom:
                for r in range(up, bottom + 1):
                    val = matrix[r][right]
                    res.append(val)
                    i += 1
                right -= 1

            if i < row* col and left <= right:
                for c in reversed(range(left, right + 1)):
                    val = matrix[bottom][c]
                    res.append(val)
                    i += 1
                bottom -= 1
                    

            if i < row* col and up <= bottom:
                for r in reversed(range(up, bottom + 1)):
                    val = matrix[r][left]
                    res.append(val)
                    i += 1
                left += 1
        
        return res
    


# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]\n
# @lcpr case=end

#
