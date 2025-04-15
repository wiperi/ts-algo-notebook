#
# @lc app=leetcode.cn id=153 lang=python3
# @lcpr version=30104
#
# [153] 寻找旋转排序数组中的最小值
#
from typing import List, Optional
from adt.py.leetcodeType import ListNode, TreeNode
# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:

        if nums[0] <= nums[-1]:
            return nums[0]

        lo, hi = 0, len(nums) -1 

        while lo <= hi:
            mid = (lo + hi) // 2
            midv = nums[mid]

            if midv >= nums[0]:
                # Middle value in in the upper section
                # Min value is in the right side
                lo = mid + 1
            else:
                # Middle value is in the bottom section
                # Min value is in the left side
                hi = mid - 1

        return nums[lo]
# @lc code=end



#
# @lcpr case=start
# [3,4,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [11,13,15,17]\n
# @lcpr case=end

#

