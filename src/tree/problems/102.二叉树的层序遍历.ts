/*
 * @lc app=leetcode.cn id=102 lang=typescript
 *
 * [102] 二叉树的层序遍历
 */

import { TreeNode } from "@/tree/BiTree";

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
  if (root === null) return [];

  const res = [];

  const q = [root];

  while (q.length !== 0) {
    const levelSize = q.length;

    const level = [];

    for (let i = 0; i < levelSize; i++) {
      const node = q.shift();
      level.push(node.val);

      if (node.left !== null) q.push(node.left)
      if (node.right !== null) q.push(node.right);
    }

    res.push(level.slice());  
  }

  return res;
};
// @lc code=end

