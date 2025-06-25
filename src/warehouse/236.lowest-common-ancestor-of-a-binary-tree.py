#
# @lc app=leetcode.cn id=236 lang=python3
# @lcpr version=30204
#
# [236] 二叉树的最近公共祖先
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        found = False
        lcs = None

        def find(root: Optional[TreeNode]):
            nonlocal found, lcs
            if not root:
                return False

            inLeft = find(root.left)
            inRight = find(root.right)
            
            # print(root.val, inLeft, inRight)

            if root is q or root is p and (inLeft or inRight):
                found = True
                lcs = root
            elif inLeft and inRight:
                found = True
                lcs = root

            return root is q or root is p or inLeft or inRight

        find(root)
        return lcs


# @lc code=end


#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n2\n
# @lcpr case=end

#
