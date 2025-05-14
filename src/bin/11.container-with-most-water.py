#
# @lc app=leetcode.cn id=11 lang=python3
# @lcpr version=30204
#
# [11] 盛最多水的容器
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        then naive approach would be iterate all comb of 2

        but f(i, j) = min(i, j) * (j - i)

        we want to make j - i as large as possible, so i == 0, j == n - 1

        now if we want to contain more water, the only solution is to change the
        shorter bar. if we change the longer, no matter what we can not have more 
        water.

        we actually avoid compute any bar diff to longer bar - and shorter bar
        '''

        def water(i, j):
            return min(height[i], height[j]) * (j - i)
        
        maxWater = 0
        n = len(height)
        l, r = 0, n - 1

        while l < r:
            localwater = water(l, r)
            maxWater = max(maxWater, localwater)

            if height[l] < height[r]:
                curr = height[l]
                l += 1
                while l < r and height[l] <= curr:
                    l += 1
            else:
                curr = height[r]
                r -= 1
                while l < r and height[r] <= curr:
                    r -= 1

        return maxWater
# @lc code=end



#
# @lcpr case=start
# [1,8,6,2,5,4,8,3,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,1]\n
# @lcpr case=end

#

