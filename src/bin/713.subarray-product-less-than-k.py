#
# @lc app=leetcode.cn id=713 lang=python3
# @lcpr version=30204
#
# [713] 乘积小于 K 的子数组
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = r = 0
        winPrt = 1
        cnt = 0
        while r < len(nums):
            winPrt *= nums[r] 
            r += 1

            while l < r and winPrt >= k:
                winPrt /= nums[l]
                l += 1
            if winPrt < k: cnt += (r - l)

        return cnt

# @lc code=end



#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#

