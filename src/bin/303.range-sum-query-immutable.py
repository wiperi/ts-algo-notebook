#
# @lc app=leetcode.cn id=303 lang=python3
# @lcpr version=30204
#
# [303] 区域和检索 - 数组不可变
#


# @lcpr-template-start
from itertools import accumulate
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.preSum[right]

        return self.preSum[right] - self.preSum[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# @lc code=end



#
# @lcpr case=start
# ["NumArray", "sumRange", "sumRange", "sumRange"][[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]\n
# @lcpr case=end

#

