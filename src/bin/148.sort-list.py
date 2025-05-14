#
# @lc app=leetcode.cn id=148 lang=python3
# @lcpr version=30204
#
# [148] 排序链表
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
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def getMid(head: Optional[ListNode]):
            slow = fast = head
            while fast and fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def merge(l: Optional[ListNode], r: Optional[ListNode]):
            dummy = ListNode()
            p = dummy

            while l and r:
                if l.val < r.val:
                    p.next = l
                    p = p.next
                    l = l.next
                else:
                    p.next = r
                    p = p.next
                    r = r.next

            if not l:
                p.next = r
            else:
                p.next = l

            return dummy.next
        
        def mergeSort(head: Optional[ListNode]):

            if not head or not head.next:
                return head

            middle = getMid(head)
            nextHead = middle.next
            middle.next = None

            l = mergeSort(head)
            r = mergeSort(nextHead)

            return merge(l, r)
        
        return mergeSort(head)

# @lc code=end



#
# @lcpr case=start
# [4,2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [-1,5,3,4,0]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

