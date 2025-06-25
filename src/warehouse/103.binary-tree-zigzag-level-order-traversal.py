#
# @lc app=leetcode.cn id=103 lang=python3
# @lcpr version=30204
#
# [103] 二叉树的锯齿形层序遍历
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = [root]
        dist = 0
        zigzag = []

        while q:
            lsize = len(q)

            level = []
            for _ in range(lsize):
                node = q.pop(0)
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            if dist % 2 == 0:
                zigzag.append(level.copy())
            else:
                zigzag.append(list(reversed(level.copy())))
            
            dist += 1
            
        return zigzag
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#

