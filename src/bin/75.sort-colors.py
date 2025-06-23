#
# @lc app=leetcode.cn id=75 lang=python3
# @lcpr version=30204
#
# [75] 颜色分类
#


# @lcpr-template-start
from typing import List, Optional
# @lcpr-template-end
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        l = 0
        for i in range(n):
            if nums[i] == 0:
                swap(i, l)
                l += 1

        for i in range(l, n):
            if nums[i] == 1:
                swap(i, l)
                l += 1

        return

# @lc code=end



#
# @lcpr case=start
# [2,0,2,1,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [2,0,1]\n
# @lcpr case=end

#

