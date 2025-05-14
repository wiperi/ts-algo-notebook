#
# @lc app=leetcode.cn id=128 lang=python3
# @lcpr version=30204
#
# [128] 最长连续序列
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        glen = 0
        gstart = -1
        for n in nums:
            if n - 1 in s:
                continue

            llen = 0
            lstart = j = n
            while j in s:
                llen += 1
                s.remove(j)
                j += 1

            if llen > glen:
                glen = llen
                gstart = lstart


        return [i for i in range(gstart, gstart + glen)]


# @lc code=end

print(Solution().longestConsecutive([100, 5, 6, 7, 4, 200, 1, 3, 2]))

#
# @lcpr case=start
# [100,4,200,1,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,7,2,5,8,4,6,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,2]\n
# @lcpr case=end

#
