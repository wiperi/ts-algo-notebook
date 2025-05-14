#
# @lc app=leetcode.cn id=109 lang=python3
# @lcpr version=30104
#
# [109] 有序链表转换二叉搜索树
#
from typing import List, Optional
from adt.py.leetcodeType import ListNode, TreeNode
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def inorder(left: int, right: int):
            nonlocal head
            if not (left <= right):
                return None
            
            mid = (left + right) // 2

            root = TreeNode()

            root.left = inorder(0, mid - 1)

            root.val = self.curr.val # type: ignore
            self.curr = self.curr.next # type: ignore


            root.right = inorder(mid + 1, right)

            return root
        
        p = head
        n = 0
        while p:
            n += 1
            p = p.next

        self.curr = head
        return inorder(0, n - 1)

        
# @lc code=end

#
# @lcpr case=start
# [-10,-3,0,5,9]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

