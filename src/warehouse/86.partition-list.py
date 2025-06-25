#
# @lc app=leetcode.cn id=86 lang=python3
# @lcpr version=30204
#
# [86] 分隔链表
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        large = ListNode()
        tLarge = large

        small = ListNode(0, head)
        tSmall = small
        while tSmall.next:
            if tSmall.next.val >= x:
                tLarge.next = tSmall.next
                tLarge = tLarge.next

                tSmall.next = tSmall.next.next
            else:
                tSmall = tSmall.next
        
        tLarge.next = None
        tSmall.next = large.next

        return small.next
# @lc code=end



#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#

