#
# @lc app=leetcode.cn id=99 lang=python3
# @lcpr version=30104
#
# [99] 恢复二叉搜索树
#
from typing import List, Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        pass

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        prev: TreeNode = None # type: ignore
        # First value that is larger than successor
        firstMax: TreeNode = None # type: ignore
        # Last value that is smaller than its predecessor
        lastMin: TreeNode = None # type: ignore

        # Example
        # [3,2,1]
        # firstMax should be 3
        # lastMin shoube be 1

        def inorder(root: Optional[TreeNode]):
            nonlocal prev, firstMax, lastMin

            if root is None:
                return

            inorder(root.left)

            if prev and prev.val > root.val:
                if firstMax is None:
                    firstMax = prev
                lastMin = root

            prev = root

            inorder(root.right)

            return

        inorder(root)

        firstMax.val, lastMin.val = lastMin.val, firstMax.val

        return


# @lc code=end


#
# @lcpr case=start
# [1,3,null,null,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,1,4,null,null,2]\n
# @lcpr case=end

#
