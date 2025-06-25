#
# @lc app=leetcode.cn id=39 lang=python3
# @lcpr version=30204
#
# [39] 组合总和
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        path = []
        pathSum = 0
        res = []
        n = len(nums)

        def comb(start):
            nonlocal pathSum

            if pathSum > target:
                return
            
            if pathSum == target:
                res.append(path.copy())
                return

            for i in range(start, n):
                path.append(nums[i])
                pathSum += nums[i]
                comb(i)
                pathSum -= nums[i]
                path.pop()

        comb(0)

        return res


# @lc code=end



#
# @lcpr case=start
# [2,3,6,7]\n7\n
# @lcpr case=end

# @lcpr case=start
# [2,3,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [2]\n1\n
# @lcpr case=end

#

