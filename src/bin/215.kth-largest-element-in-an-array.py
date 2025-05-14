#
# @lc app=leetcode.cn id=215 lang=python3
# @lcpr version=30204
#
# [215] 数组中的第K个最大元素
#


# @lcpr-template-start
from heapq import heappop, heappush
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        there will be k - 1 elements > than target

        we use a small heap of size k

        after go through all value, the top value is our target.
        ther will be k - 1 value > it.
        '''

        pq = []


        for v in nums:
            heappush(pq, v)

            if len(pq) > k:
                heappop(pq)
            
        return pq[0]
# @lc code=end



#
# @lcpr case=start
# 2\n
# @lcpr case=end

# @lcpr case=start
# 4\n
# @lcpr case=end

#

