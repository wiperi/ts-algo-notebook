#
# @lc app=leetcode.cn id=2058 lang=python3
# @lcpr version=30204
#
# [2058] 找出临界点之间的最小和最大距离
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
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        points = []
        def recur(head: Optional[ListNode], i):

            if not head or not head.next or not head.next.next:
                return
            
            recur(head.next, i + 1)

            if head.val < head.next.val > head.next.next.val or (
                head.val > head.next.val < head.next.next.val
            ):
                points.append(i)

        recur(head, 0)

        if len(points) < 2:
            return [-1 , -1]

        points.sort()
        maxDiff = points[-1] - points[0]
        minDiff = float('inf')
        for i in range(1, len(points)):
            if points[i] - points[i - 1] < minDiff:
                minDiff = points[i] - points[i - 1]

        return [minDiff, maxDiff]
# @lc code=end



#
# @lcpr case=start
# [3,1]\n
# @lcpr case=end

# @lcpr case=start
# [5,3,1,2,5,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,2,3,2,2,2,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,3,2]\n
# @lcpr case=end

#

