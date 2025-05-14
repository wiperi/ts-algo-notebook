#
# @lc app=leetcode.cn id=15 lang=python3
# @lcpr version=30204
#
# [15] 三数之和
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        i = 0
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo = i + 1
            hi = n - 1
            target = -nums[i]

            while lo < hi:
                s = nums[lo] + nums[hi]

                if s == target:
                    res.append([nums[i], nums[lo], nums[hi]])

                    lo += 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1

                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
                elif s > target:
                    hi -= 1
                elif s < target:
                    lo += 1

        return res


# @lc code=end


#
# @lcpr case=start
# [-1,0,1,2,-1,-4]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0]\n
# @lcpr case=end

#
