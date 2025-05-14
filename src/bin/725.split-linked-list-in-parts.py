#
# @lc app=leetcode.cn id=725 lang=python3
# @lcpr version=30204
#
# [725] 分隔链表
#


# @lcpr-template-start
from math import ceil
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
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        a = head
        while a:
            n += 1
            a = a.next

        size = ceil(n / k)
        redundant = size * k - n

        parts = [size] * k
        for i in range(k - redundant, k):
            parts[i] -= 1


        res = []
        for part in parts:
            res.append(head)
            t = 0
            while t < part - 1:
                head = head.next
                t += 1
            
            if head:
                tmp = head.next
                head.next = None
                head = tmp

        return res

# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7,8,9,10]\n3\n
# @lcpr case=end

#

