#
# @lc app=leetcode.cn id=442 lang=python3
# @lcpr version=30204
#
# [442] 数组中重复的数据
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        for i in range(n):
            while nums[nums[i] - 1] != nums[i]:
                swap(i, nums[i] - 1)
            
        res = []
        for i in range(n):
            if i + 1 != nums[i]:
                res.append(nums[i])

        return res

# @lc code=end



#
# @lcpr case=start
# [4,3,2,7,8,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

