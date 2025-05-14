#
# @lc app=leetcode.cn id=18 lang=python3
# @lcpr version=30204
#
# [18] 四数之和
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(nums: List[int], t) -> List[List[int]]:
            n = len(nums)
            i = 0
            res = []
            for i in range(n - 2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                lo = i + 1
                hi = n - 1
                target = t - nums[i]

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
        
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            subres = threeSum(nums[i + 1:], target - nums[i])
            res.extend([nums[i]] + a for a in subres)

        return res
# @lc code=end



#
# @lcpr case=start
# [1,0,-1,0,-2,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,2,2]\n8\n
# @lcpr case=end

#

