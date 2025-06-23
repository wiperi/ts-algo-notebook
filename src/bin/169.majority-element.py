#
# @lc app=leetcode.cn id=169 lang=python3
# @lcpr version=30204
#
# [169] 多数元素
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        cand = nums[0]
        weight = 1
        for i in range(1,  n):
            if nums[i] == cand:
                weight += 1
            else:
                weight -= 1
                if weight == 0:
                    cand = nums[i]
                    weight = 1

        return cand

# @lc code=end



#
# @lcpr case=start
# [3,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,1,1,1,2,2]\n
# @lcpr case=end

#

