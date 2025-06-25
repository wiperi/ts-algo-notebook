#
# @lc app=leetcode.cn id=1290 lang=python3
# @lcpr version=30204
#
# [1290] 二进制链表转整数
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
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
        n = 0
        res = 0
        def foo(head: Optional[ListNode]):
            nonlocal n, res
            if not head:
                return
            foo(head.next)

            if head.val == 1:
                res |= (1 << n)
            n += 1

        foo(head)

        return res


# @lc code=end



#
# @lcpr case=start
# [1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,0]\n
# @lcpr case=end

#

