#
# @lc app=leetcode.cn id=112 lang=python3
# @lcpr version=30204
#
# [112] 路径总和
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        s = 0
        found = False

        def dfs(root: Optional[TreeNode]):
            nonlocal s, found

            if not root:
                return
            s += root.val

            if s == targetSum and not root.left and not root.right:
                found = True
                return

            dfs(root.left)
            dfs(root.right)
            s -= root.val

            return
        
        dfs(root)
        return found


# @lc code=end


#
# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,null,1]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# []\n0\n
# @lcpr case=end

#
