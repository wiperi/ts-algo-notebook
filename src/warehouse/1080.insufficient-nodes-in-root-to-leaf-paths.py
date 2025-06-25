#
# @lc app=leetcode.cn id=1080 lang=python3
# @lcpr version=30204
#
# [1080] 根到叶路径上的不足节点
#


# @lcpr-template-start
from turtle import rt
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
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:

        def dfs(root: Optional[TreeNode], s):

            s += root.val

            if root.left is root.right:
                return None if s < limit else root
            
            if root.left: root.left = dfs(root.left, s)
            if root.right: root.right = dfs(root.right, s)

            return None if root.left is root.right else root

        return dfs(root, 0)
        



# @lc code=end


#
# @lcpr case=start
# [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,4,8,11,null,17,4,7,1,null,null,5,3]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,-3,-5,null,4,null]\n-1\n
# @lcpr case=end

#
