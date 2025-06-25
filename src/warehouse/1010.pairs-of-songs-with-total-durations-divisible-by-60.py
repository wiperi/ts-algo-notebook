#
# @lc app=leetcode.cn id=1010 lang=python3
# @lcpr version=30204
#
# [1010] 总持续时间可被 60 整除的歌曲
#


# @lcpr-template-start
from collections import defaultdict
import heapq
from math import ceil
from typing import Counter, List, Optional

from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        """
        find a segment that not zero

        find min value
        set to 0
        """
        n = len(nums)
        cnt = 0
        vis = [False] * n

        def dfs(l, r):
            if not (l <= r):
                return

            nonlocal cnt, vis

            minval = min(nums[l : r + 1])

            if minval != 0:
                cnt += 1

            for i in range(l, r + 1):
                if nums[i] == minval:
                    nums[i] = 0

                    leftBound = i - 1
                    while leftBound >= 0 and nums[leftBound] >= nums[leftBound + 1] and not vis[leftBound]:
                        vis[leftBound] = True
                        if nums[leftBound] > nums[leftBound + 1]: cnt += 1
                        leftBound -= 1

                    dfs(l, leftBound)

                    rightBound = i + 1
                    while rightBound <= r and nums[rightBound] >= nums[rightBound - 1] and not vis[rightBound]:
                        vis[rightBound] = True
                        if nums[rightBound] > nums[rightBound - 1]: cnt += 1
                        rightBound += 1

                    dfs(rightBound, r)

        dfs(0, n - 1)
        return cnt


# @lc code=end


print(Solution().minOperations([1,2,1,2,1,2]))

#
# @lcpr case=start
# [30,20,150,100,40]\n
# @lcpr case=end

# @lcpr case=start
# [60,60,60]\n
# @lcpr case=end

#
