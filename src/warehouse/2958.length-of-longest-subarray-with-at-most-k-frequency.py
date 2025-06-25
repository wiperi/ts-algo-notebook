#
# @lc app=leetcode.cn id=2958 lang=python3
# @lcpr version=30204
#
# [2958] 最多 K 个重复元素的最长子数组
#


# @lcpr-template-start
from collections import defaultdict
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        win = defaultdict(int)
        l = r = 0
        mlen = 0
        while r < len(nums):
            add = nums[r]
            win[add] += 1
            r += 1

            while l < len(nums) and win[add] > k:
                win[nums[l]] -= 1
                l += 1

            mlen = max(mlen, r - l)
        
        return mlen
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1,2,3,1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,1,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5,5,5,5,5]\n4\n
# @lcpr case=end

#

