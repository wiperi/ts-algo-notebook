#
# @lc app=leetcode.cn id=437 lang=python3
# @lcpr version=30204
#
# [437] 路径总和 III
#


# @lcpr-template-start
from collections import defaultdict
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        path = defaultdict(int)
        path[0] = 1
        res = 0

        def dfs(root: Optional[TreeNode], currSum):
            nonlocal res
            if not root:
                return

            currSum += root.val
            res += path[currSum - targetSum]

            path[currSum] += 1

            dfs(root.left, currSum)
            dfs(root.right, currSum)

            path[currSum] -= 1
        
        dfs(root, 0)
        return res
# @lc code=end



#
# @lcpr case=start
# [10,5,-3,3,2,null,11,3,-2,null,1]\n8\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

#

