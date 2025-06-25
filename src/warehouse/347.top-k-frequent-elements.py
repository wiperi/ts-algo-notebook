#
# @lc app=leetcode.cn id=347 lang=python3
# @lcpr version=30204
#
# [347] 前 K 个高频元素
#


# @lcpr-template-start
from bisect import bisect_right
from heapq import heappop, heappush
from typing import Counter, List, Optional, OrderedDict
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)

        pq = []

        for key, freq in mp.items():
            heappush(pq, (freq, key))

            if len(pq) > k:
                heappop(pq)

        return [t[1] for t in pq]



        
# @lc code=end



#
# @lcpr case=start
# [1,1,1,2,2,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n2\n
# @lcpr case=end

#

