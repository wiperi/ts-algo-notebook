#
# @lc app=leetcode.cn id=679 lang=python3
# @lcpr version=30204
#
# [679] 24 点游戏
#


# @lcpr-template-start
from itertools import accumulate, combinations, pairwise, permutations
from typing import List, Optional
from lct import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        DIV = 0
        ADD = 1
        MUL = 2
        SUB = 3
        EPSILON = 1e-6

        res = False

        def dfs(nums: list):
            if len(nums) == 1:
                if abs(nums[0] - 24) < EPSILON:
                    nonlocal res
                    res = True
                return

            permus = permutations(list(range(len(nums))), 2)
            for i, j in permus:
                a = nums[i]
                b = nums[j]

                new = []
                for k in range(len(nums)):
                    if k == i or k == j:
                        continue
                    new.append(nums[k])

                for op in range(4):
                    if op == DIV and b != 0:
                        dfs(new + [a / b])
                    elif op == ADD:
                        dfs(new + [a + b])
                    elif op == MUL:
                        dfs(new + [a * b])
                    elif op == SUB:
                        dfs(new + [a - b])

        dfs(cards.copy())
        return res
                


# @lc code=end


# Solution().judgePoint24([12,12])
#
# @lcpr case=start
# [4, 1, 8, 7]\n
# @lcpr case=end

# @lcpr case=start
# [1, 2, 1, 2]\n
# @lcpr case=end

#
