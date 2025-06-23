#
# @lc app=leetcode.cn id=1695 lang=python3
# @lcpr version=30204
#
# [1695] 删除子数组的最大得分
#


# @lcpr-template-start
from collections import defaultdict
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # 不含重复元素的最大子数组

        l, r = 0, 0
        win = set()
        winSum = 0
        res = 0
        while r < len(nums):
            while nums[r] in win:
                winSum -= nums[l]
                win.discard(nums[l])
                l += 1

            win.add(nums[r])
            winSum += nums[r]
            r += 1

            res = max(res, winSum)

        return res


# @lc code=end



#
# @lcpr case=start
# [4,2,4,5,6]\n
# @lcpr case=end

# @lcpr case=start
# [5,2,1,2,5,2,1,2,5]\n
# @lcpr case=end

#

