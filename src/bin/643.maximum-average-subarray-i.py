#
# @lc app=leetcode.cn id=643 lang=python3
# @lcpr version=30204
#
# [643] 子数组最大平均数 I
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])

        average = s / k
        res = average

        l, r = 0, k
        n = len(nums)
        while r < n:
            average -= (nums[l] / k)
            l += 1

            average += (nums[r] / k)
            r += 1

            res = max(res, average)

        return res

            
# @lc code=end



#
# @lcpr case=start
# [1,12,-5,-6,50,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n
# @lcpr case=end

#

