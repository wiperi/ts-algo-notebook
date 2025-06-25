#
# @lc app=leetcode.cn id=238 lang=python3
# @lcpr version=30204
#
# [238] 除自身以外数组的乘积
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = nums.copy()

        l = 1
        for i in range(n):
            res[i] = l
            l *= nums[i]

        r = 1
        for i in reversed(range(n)):
            res[i] *= r
            r *= nums[i]

        return res

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [-1,1,0,-3,3]\n
# @lcpr case=end

#

