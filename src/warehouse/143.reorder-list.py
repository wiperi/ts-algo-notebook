#
# @lc app=leetcode.cn id=143 lang=python3
# @lcpr version=30204
#
# [143] 重排链表
#


# @lcpr-template-start
from time import pthread_getcpuclockid
from typing import List, Optional

from httpx import NetRCAuth
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return head

        n = 0
        p = head
        while p:
            n += 1
            p = p.next

        times = n // 2

        dummy = ListNode()
        t = dummy
        left = head

        def recur(head: Optional[ListNode]):
            nonlocal times, t, left, n

            if not head:
                return
            
            recur(head.next)

            if times <= 0:
                return

            times -= 1
            t.next = left
            t = t.next
            left = left.next

            t.next = head
            t = t.next

        recur(head)
        
        if n % 2 == 1:
            t.next = left
            t = t.next
            t.next = None
        else:
            t.next = None

        return dummy.next






# @lc code=end


#
# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

#
