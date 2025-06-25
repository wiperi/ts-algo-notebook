#
# @lc app=leetcode.cn id=2105 lang=python3
# @lcpr version=30204
#
# [2105] 给植物浇水 II
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        
        alice = capacityA
        bob = capacityB

        n = len(plants)

        i , j = 0, n - 1

        res = 0
        while i < j:
            if alice < plants[i]:
                alice = capacityA
                res += 1
            alice -= plants[i]

            if bob < plants[j]:
                bob = capacityB
                res += 1
            bob -= plants[j]

            i += 1
            j -= 1

        if i == j and max(alice, bob) < plants[i]:
            res += 1

        return res
# @lc code=end



#
# @lcpr case=start
# [2,2,3,3]\n5\n5\n
# @lcpr case=end

# @lcpr case=start
# [2,2,3,3]\n3\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n10\n8\n
# @lcpr case=end

#

