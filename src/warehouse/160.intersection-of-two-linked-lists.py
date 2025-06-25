#
# @lc app=leetcode.cn id=160 lang=python3
# @lcpr version=30204
#
# [160] 相交链表
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, ha: ListNode, hb: ListNode) -> Optional[ListNode]:
        """
        Elegant solution using the two-pointer technique.
        If two linked lists intersect, pointers will meet after switching paths.
        If they don't intersect, both pointers will reach None simultaneously.
        """
        if not ha or not hb:
            return None
            
        a, b = ha, hb
        
        # When a pointer reaches the end, redirect it to the head of the other list
        # This ensures both pointers travel the same distance before meeting
        while a != b:
            a = hb if a is None else a.next
            b = ha if b is None else b.next
            
        return a  # Either the intersection point or None if no intersection

        

# @lc code=end



#
# @lcpr case=start
# 8\n[4,1,8,4,5]\n[5,6,1,8,4,5]\n2\n3\n
# @lcpr case=end

# @lcpr case=start
# 2\n[1,9,1,2,4]\n[3,2,4]\n3\n1\n
# @lcpr case=end

# @lcpr case=start
# 0\n[2,6,4]\n[1,5]\n3\n2\n
# @lcpr case=end

#

