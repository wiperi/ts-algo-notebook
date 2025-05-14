/*
 * @lc app=leetcode.cn id=222 lang=typescript
 *
 * [222] 完全二叉树的节点个数
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

// Best case O(1)
function countNodes(root: TreeNode | null): number {
  // For a complete binary tree. One of its sub tree must be full binary tree.
  // And we can use formula directly calculate the size of full binary tree.

  if (root === null) {
    return 0;
  }

  let l = root;
  let r = root;

  let lHeight = 1;
  let rHeight = 1;

  // Find the height of left sub tree
  while (l.left !== null) {
    l = l.left;
    lHeight++;
  }

  // Find the height of right sub tree
  while (r.right !== null) {
    r = r.right;
    rHeight++;
  }

  if (lHeight === rHeight) {
    // Current tree is full binary tree, return result directly
    return 2 ** lHeight - 1;
  }

  return 1 + countNodes(root.left) + countNodes(root.right);
}
// @lc code=end

// O(n)
(function countNodes(root: TreeNode | null): number {
  if (root === null) return 0;

  let res = 0;
  res += countNodes(root.left);
  res += countNodes(root.right);

  return res + 1;
});
