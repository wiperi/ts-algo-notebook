#
# @lc app=leetcode.cn id=865 lang=python3
# @lcpr version=30204
#
# [865] 具有所有最深节点的最小子树
#


# @lcpr-template-start
from collections import defaultdict
from logging import _Level
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
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        mp = defaultdict(int)

        def dfs(root: Optional[TreeNode], level):
            if not root:
                return
            
            mp[level] += 1
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        dfs(root, 0)

        arr = sorted(mp.items(), key=lambda a: a[0], reverse=True)
        maxDepth = arr[0][0]
        numDeepest = arr[0][1]
        res = None

        print(maxDepth)
        print(numDeepest)

        def fn(root: Optional[TreeNode], l):
            nonlocal res
            if root.left is root.right:
                if l == maxDepth and numDeepest == 1:
                    res = root
                    return 0
                return 1 if l == maxDepth else 0

            left = right = 0
            if root.left: left = fn(root.left, l + 1) 
            if root.right: right = fn(root.right, l + 1)

            if left + right == numDeepest:
                res = root
                return 0

            return left + right + (1 if l == maxDepth else 0)
        
        fn(root, 0)

        return res

# @lc code=end



#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,3,null,2]\n
# @lcpr case=end

#

