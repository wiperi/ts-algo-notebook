#
# @lc app=leetcode.cn id=82 lang=python3
# @lcpr version=30204
#
# [82] 删除排序链表中的重复元素 II
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        p = dummy
        while p and p.next and p.next.next:
            if p.next.val == p.next.next.val:
                dup_val = p.next.val
                j = p.next.next
                while j and j.val == dup_val:
                    j = j.next
                p.next = j
            else:
                p = p.next

        return dummy.next


# @lc code=end



#
# @lcpr case=start
# [1,2,3,3,4,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,2,3]\n
# @lcpr case=end

#

