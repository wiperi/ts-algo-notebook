#
# @lc app=leetcode.cn id=239 lang=python3
# @lcpr version=30204
#
# [239] 滑动窗口最大值
#


# @lcpr-template-start
from collections import defaultdict
from heapq import heapify, heappop, heappush
import heapq
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)

        nums = [-1 * v for v in nums]
        pq = []
        heapify(pq)
        freq = defaultdict(int)
        for i in range(k):
            freq[nums[i]] += 1
            heappush(pq, nums[i])

        res = []
        res.append(pq[0])
        # print(pq)

        l, r = 0, k

        while r < n:
            # when the deleting value is maximum and only one left in window
            # then pq pop
            # if nums[l] == pq[0] and freq[nums[l]] == 1:
            #     while pq and pq[0] == nums[l]:
            #         heappop(pq)
            freq[nums[l]] -= 1
            while pq and freq[pq[0]] == 0:
                heappop(pq)

            freq[nums[r]] += 1
            heappush(pq, nums[r])

            # print(pq)
            # print(freq)
                
            res.append(pq[0])

            l += 1
            r += 1

        return [-1 * v for v in res]


# @lc code=end



#
# @lcpr case=start
# [1,3,-1,-3,5,3,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [9,10,9,-7,-4,-8,2,-6]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,-1]\n1\n
# @lcpr case=end

#

