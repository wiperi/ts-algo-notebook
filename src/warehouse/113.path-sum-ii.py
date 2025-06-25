#
# @lc app=leetcode.cn id=113 lang=python3
# @lcpr version=30204
#
# [113] 路径总和 II
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        s = 0
        path = []
        res = []

        def dfs(root: Optional[TreeNode]):
            nonlocal s

            if not root:
                return
            s += root.val
            path.append(root.val)

            if s == targetSum and not root.left and not root.right:
                res.append(path.copy())

            dfs(root.left)
            dfs(root.right)
            s -= root.val
            path.pop()

            return
        
        dfs(root)
        return res
# @lc code=end



#
# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

#

