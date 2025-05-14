#
# @lc app=leetcode.cn id=646 lang=python3
# @lcpr version=30104
#
# [646] 最长数对链
#
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lc code=start
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])

        # dp(i) = of paris[0..i], longest len of pair list
        # prevTail = the right side value of previous pair list
        
        n = len(pairs)

        dp = [1] * n
        prevTail = pairs[0][1]

        for i in range(1, n):
            p = pairs[i]
            head = p[0]
            tail = p[1]

            if head <= prevTail:
                # There is overlap, discard current pair
                dp[i] = dp[i - 1]
                continue
            else:
                # Add current pair to the list, and update prevTail
                dp[i] = dp[i - 1] + 1
                prevTail = tail

        return dp[-1]
        
# @lc code=end



#
# @lcpr case=start
# [[1,2], [2,3], [3,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]\n
# @lcpr case=end

#

