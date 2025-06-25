#
# @lc app=leetcode.cn id=525 lang=python3
# @lcpr version=30204
#
# [525] 连续数组
#


# @lcpr-template-start
from collections import defaultdict
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ind = {}
        ind[0] = -1

        n = len(nums)
        s = 0
        mlen = 0
        for i in range(n):
            if nums[i] == 0:
                s -= 1
            else:
                s += 1

            if s in ind: mlen = max(mlen, i - ind[s])

            if s not in ind: ind[s] = i

        return mlen


# @lc code=end


#
# @lcpr case=start
# [0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,1,1,1,1,0,0,0]\n
# @lcpr case=end

#
