#
# @lc app=leetcode.cn id=1658 lang=python3
# @lcpr version=30204
#
# [1658] 将 x 减到 0 的最小操作数
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # x == sum(two side of array)
        # sum(array) = sum(middle) - sum(two side) = sum(middle) - x
        # find a longest window , that sum(window in the middle) = sum(array) - x


        tSum = sum(nums) - x

        l = r = 0
        winSum = 0
        mlen = -1
        while r < len(nums):
            winSum += nums[r]
            r += 1

            while l < r and winSum > tSum:
                winSum -= nums[l]
                l += 1

            if winSum == tSum:
                mlen = max(mlen, r - l)

        return (len(nums) - mlen) if mlen != -1 else -1
# @lc code=end



#
# @lcpr case=start
# [1,1,4,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [5,6,7,8,9]\n4\n
# @lcpr case=end

# @lcpr case=start
# [3,2,20,1,1,3]\n10\n
# @lcpr case=end

#

