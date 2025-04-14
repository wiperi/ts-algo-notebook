#
# @lc app=leetcode.cn id=437 lang=python3
# @lcpr version=30104
#
# [437] 路径总和 III
#
from collections import defaultdict
from typing import List, Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Prefix Sum
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        res = 0
        # pathSum -> frequency in the tree
        map = defaultdict(int)
        map[0] = 1

        def dfs(root: Optional[TreeNode], pathSum: int):
            nonlocal res

            if not root:
                return

            pathSum += root.val

            res += map[pathSum - targetSum]

            map[pathSum] += 1
            dfs(root.left, pathSum)
            dfs(root.right, pathSum)
            map[pathSum] -= 1

        dfs(root, 0)

        return res


class BruteForce:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.res = 0

        def check(root: Optional[TreeNode], pathSum: int):
            if not root:
                return

            pathSum += root.val
            # print(root.val, pathSum)
            if pathSum == targetSum:
                self.res += 1

            check(root.left, pathSum)
            check(root.right, pathSum)

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return

            check(root, 0)

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.res


# @lc code=end


#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#
