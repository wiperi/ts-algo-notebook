/*
 * @lc app=leetcode.cn id=1448 lang=typescript
 *
 * [1448] 统计二叉树中好节点的数目
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

function goodNodes(root: TreeNode | null): number {
  // Record the largest value in current path
  
  let res = 0;
  dfs(root, -Infinity);

  return res;

  function dfs(root: TreeNode | null, max: number) {
    if (root === null) return;

    if (root.val >= max) {
      res++;
    }

    dfs(root.left, Math.max(root.val, max));
    dfs(root.right, Math.max(root.val, max));
  }
}
// @lc code=end
