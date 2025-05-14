#
# @lc app=leetcode.cn id=328 lang=python3
# @lcpr version=30204
#
# [328] 奇偶链表
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
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        leven = ListNode()
        lodd = ListNode()
        even = leven
        odd = lodd

        p = head
        i = 0
        while p:
            if i % 2 == 0:
                even.next = p
                even = even.next
            else:
                odd.next = p
                odd = odd.next

            i += 1
            p = p.next

        odd.next = None
        even.next = lodd.next

        return leven.next
        

# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3,5,6,4,7]\n
# @lcpr case=end

#

