/*
 * @lc app=leetcode.cn id=102 lang=typescript
 *
 * [102] 二叉树的层序遍历
 */

import { TreeNode } from '@/adt/BiTree';

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
function levelOrder(root: TreeNode | null): number[][] {

  if (root === null) {
    return [];
  }

  const queue = [root];
  const res = [];

  while (queue.length != 0) {

    const levelSize = queue.length;
    const level = [];

    for (let i = 0; i < levelSize; i++) {
      const curr = queue.shift();
      level.push(curr.val);

      if (curr.left) queue.push(curr.left);
      if (curr.right) queue.push(curr.right);
    }

    res.push(level.slice());
  }

  return res;
}
// @lc code=end

export {};
