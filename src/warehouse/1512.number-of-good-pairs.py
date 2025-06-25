#
# @lc app=leetcode.cn id=1512 lang=python3
# @lcpr version=30204
#
# [1512] 好数对的数目
#


# @lcpr-template-start
from collections import defaultdict
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        mp = defaultdict(int)

        res = 0
        for i, v in enumerate(nums):
            if v in mp:
                res += mp[v]

            mp[v] += 1

        return res


# @lc code=end


#
# @lcpr case=start
# [1,2,3,1,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#
