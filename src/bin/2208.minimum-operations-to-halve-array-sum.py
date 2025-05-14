#
# @lc app=leetcode.cn id=2208 lang=python3
# @lcpr version=30204
#
# [2208] 将数组和减半的最少操作次数
#


# @lcpr-template-start
from heapq import heappop, heappush, heappushpop
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        '''
        init a heap

        each time create a 
        '''

        s = sum(nums)
        n = len(nums)

        pq = []
        for v in nums:
            heappush(pq, -v)

        shrinked = 0
        count = 0
        while shrinked < (s / 2):
            count += 1

            half = -heappop(pq) / 2
            shrinked += half

            heappush(pq, -half)
        return count

        
# @lc code=end



#
# @lcpr case=start
# [5,19,8,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,8,20]\n
# @lcpr case=end

#

