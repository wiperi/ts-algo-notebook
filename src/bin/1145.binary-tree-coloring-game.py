#
# @lc app=leetcode.cn id=1145 lang=python3
# @lcpr version=30204
#
# [1145] 二叉树着色游戏
#


# @lcpr-template-start
from typing import List, Optional

from numpy import true_divide
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
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:

        parent = 0
        leftChild = 0
        rightChild = 0

        def numOfNodes(root: Optional[TreeNode]):
            nonlocal leftChild, rightChild
            if not root:
                return 0
            
            left = numOfNodes(root.left)
            right = numOfNodes(root.right)

            if root.val == x:
                leftChild = left
                rightChild = right

            return left + right + 1

        numOfNodes(root)

        parent = n - (leftChild + rightChild + 1)

        if (
            parent > (leftChild + rightChild)
            or leftChild > (parent + rightChild)
            or rightChild > (parent + leftChild)
        ):
            return True
        else:
            return False
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10,11]\n11\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n3\n1\n
# @lcpr case=end

#

