/*
 * @lc app=leetcode.cn id=104 lang=typescript
 *
 * [104] 二叉树的最大深度
 */

import { TreeNode } from '@/tree/BiTree';

// @lc code=start
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

// DFS思想
function maxDepth(root: TreeNode | null): number {
  if (root === null) return 0;

  return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
}
// @lc code=end

// 回溯思想
(function maxDepth(root: TreeNode | null): number {
  if (root == null) {
    return 0;
  }

  let res = 1;
  traverse(root, 1);
  return res;

  function traverse(root: TreeNode, depth: number) {
    if (root === null) return;

    res = Math.max(res, depth);

    traverse(root.left, depth + 1);
    traverse(root.right, depth + 1);
  }
});
