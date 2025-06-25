#
# @lc app=leetcode.cn id=1493 lang=python3
# @lcpr version=30204
#
# [1493] 删掉一个元素以后全为 1 的最长子数组
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        zero = 0
        mlen = 0
        while r < len(nums):
            if nums[r] == 0:
                zero += 1
            r += 1

            while zero > 1:
                if nums[l] == 0:
                    zero -= 1
                l += 1

            mlen = max(mlen, r - l - 1)

        return mlen
# @lc code=end



#
# @lcpr case=start
# [1,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,0,1,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1]\n
# @lcpr case=end

#

