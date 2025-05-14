#
# @lc app=leetcode.cn id=3319 lang=python3
# @lcpr version=30204
#
# [3319] 第 K 大的完美二叉子树的大小
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

        res = []

        def dfs(root: Optional[TreeNode]) -> tuple:
            if not root:
                return 0, 0

            ls, lh = dfs(root.left)
            rs, rh = dfs(root.right)
            height = max(lh, rh) + 1
            size = ls + rs + 1

            if 2**height - 1 == size:
                res.append(size)

            return size, height
        
        dfs(root)

        res.sort()
        return res[-k] if k <= len(res) else -1


# @lc code=end


#
# @lcpr case=start
# [5,3,6,5,2,5,7,1,8,null,null,6,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,null,4]\n3\n
# @lcpr case=end

#
