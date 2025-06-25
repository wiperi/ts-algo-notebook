#
# @lc app=leetcode.cn id=704 lang=python3
# @lcpr version=30204
#
# [704] 二分查找
#


# @lcpr-template-start
from bisect import bisect_left
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect_left(nums, target)
        if i >= len(nums) or nums[i] != target:
            return -1
        else:
            return i
# @lc code=end



#
# @lcpr case=start
# [-1,0,3,5,9,12]\n9\n
# @lcpr case=end

# @lcpr case=start
# [-1,0,3,5,9,12]\n2\n
# @lcpr case=end

#

