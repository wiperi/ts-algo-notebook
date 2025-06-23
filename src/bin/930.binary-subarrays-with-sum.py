#
# @lc app=leetcode.cn id=930 lang=python3
# @lcpr version=30204
#
# [930] 和相同的二元子数组
#


# @lcpr-template-start
from collections import defaultdict
from itertools import accumulate
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l1 = l2 = r = s1 = s2 = res = 0
        while r < len(nums):
            s1 += nums[r]
            s2 += nums[r]
            r += 1

            while l1 < r and s1 >= goal:
                s1 -= nums[l1]
                l1 += 1

            while l2 < r and s2 >= goal + 1:
                s2 -= nums[l2]
                l2 += 1

            res += (l1 - l2)

        return res
# @lc code=end



#
# @lcpr case=start
# [1,0,1,0,1]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,0,0,0]\n0\n
# @lcpr case=end

#

