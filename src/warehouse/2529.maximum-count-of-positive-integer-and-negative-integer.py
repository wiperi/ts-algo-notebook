#
# @lc app=leetcode.cn id=2529 lang=python3
# @lcpr version=30204
#
# [2529] 正整数和负整数的最大计数
#


# @lcpr-template-start
from bisect import bisect_left, bisect_right
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        i = bisect_right(nums, 0)
        pos = len(nums) - i
        j = bisect_left(nums, 0)
        neg = j - 0

        return max(neg, pos)
# @lc code=end



#
# @lcpr case=start
# [-2,-1,-1,1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-3,-2,-1,0,0,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,20,66,1314]\n
# @lcpr case=end

#

