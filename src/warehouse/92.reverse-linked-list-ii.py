#
# @lc app=leetcode.cn id=92 lang=python3
# @lcpr version=30204
#
# [92] 反转链表 II
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]):
            if not head or not head.next:
                return head
            
            last = reverse(head.next)

            head.next.next = head
            head.next = None

            return last
        
        # Handle edge case
        if not head or left == right:
            return head

        dum = ListNode(0, head)
        prev = dum
        for _ in range(left - 1):
            prev = prev.next

        leftNode = prev.next
        
        # Find the right node
        rightNode = leftNode
        for _ in range(right - left):
            rightNode = rightNode.next
            
        # Save the node after right node
        after = rightNode.next
        
        # Cut the sublist that needs to be reversed
        prev.next = None
        rightNode.next = None
        
        # Reverse the sublist and connect
        prev.next = reverse(leftNode)
        leftNode.next = after

        return dum.next




# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n4\n
# @lcpr case=end

# @lcpr case=start
# [5]\n1\n1\n
# @lcpr case=end

#

