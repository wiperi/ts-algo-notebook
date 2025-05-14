#
# @lc app=leetcode.cn id=33 lang=python3
# @lcpr version=30104
#
# [33] 搜索旋转排序数组
#
from typing import List, Optional
from adt.py.leetcodeType import ListNode, TreeNode


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if target == nums[mid]:
                return mid
            elif nums[mid] >= nums[0]:
                # mid is in the upper section
                if nums[0] <= target < nums[mid]:
                    # target is in the left side
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # mid is in the bottom section
                if nums[mid] < target <= nums[-1]:
                    # target is in the right side
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1


# @lc code=end


#
# @lcpr case=start
# [4,5,6,7,0,1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [4,5,6,7,0,1,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1]\n0\n
# @lcpr case=end

#
