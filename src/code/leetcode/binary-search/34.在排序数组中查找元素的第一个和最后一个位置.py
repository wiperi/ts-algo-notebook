#
# @lc app=leetcode.cn id=34 lang=python3
# @lcpr version=30104
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List, Optional
from adt.py.leetcodeType import ListNode, TreeNode


# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Find the index of target
        def findIndex(lo, hi, target):
            while lo <= hi:
                mid = (lo + hi) // 2

                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return -1

        # Find the left bound
        def leftBound(lo, hi, target):
            while lo <= hi:
                mid = (lo + hi) // 2

                if target == nums[mid]:
                    hi = mid - 1
                elif target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return lo

        # Find the right bound
        def rightBound(lo, hi, target):
            while lo <= hi:
                mid = (lo + hi) // 2

                if target == nums[mid]:
                    lo = mid + 1
                elif target > nums[mid]:
                    lo = mid + 1
                else:
                    hi = mid - 1

            return hi

        targetIndex = findIndex(0, len(nums) - 1, target)

        if targetIndex == -1:
            return [-1, -1]

        return [
            leftBound(0, targetIndex, target),
            rightBound(targetIndex, len(nums) - 1, target),
        ]


# @lc code=end


#
# @lcpr case=start
# [5,7,7,8,8,10]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,7,7,8,8,10]\n6\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#
