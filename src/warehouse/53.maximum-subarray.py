#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30204
#
# [53] 最大子数组和
#


# @lcpr-template-start
from typing import List, Optional
from math import inf
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        mxsum = -inf
        for i in range(n):
            for j in range(i + 1):
                s = sum(nums[j: i + 1])
                mxsum = max(mxsum, s)
        return mxsum


         

# @lc code=end

nums = [1,-2,4,1,2,-4,1]

#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

