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
        st = []
        n = len(nums)
        res = []

        for r in range(n):
            while st and nums[r] > nums[st[-1]]:
                st.pop()
            st.append(r)

            if r < k - 1:
                continue
            
            res.append(nums[st[0]])

            l = r - k + 1
            if nums[l] == nums[st[0]]:
                st.pop(0)

        return res



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

