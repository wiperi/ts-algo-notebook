#
# @lc app=leetcode.cn id=48 lang=python3
# @lcpr version=30204
#
# [48] 旋转图像
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def reverse(arr: list):
            lo, hi = 0, len(arr) - 1

            while lo < hi:
                arr[lo], arr[hi] = arr[hi], arr[lo]

                lo += 1
                hi -= 1

            return

        n = len(matrix)

        for i in range(n):
            for j in range(i + 1):
                matrix[i][i - j], matrix[i - j][i] = matrix[i - j][i], matrix[i][i - j]


        for r in matrix:
            reverse(r)

        return

# @lc code=end


#
# @lcpr case=start
# [[1,2,3],[4,5,6],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]\n
# @lcpr case=end

#
