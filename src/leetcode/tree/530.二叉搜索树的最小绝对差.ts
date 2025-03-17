/*
 * @lc app=leetcode.cn id=530 lang=typescript
 *
 * [530] 二叉搜索树的最小绝对差
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

function getMinimumDifference(root: TreeNode | null): number {

  let minDiff = 10 ** 5;
  let prev = 10 ** 5;
  traverse(root);

  return minDiff;

  function traverse(root: TreeNode) {
    if (root == null) return;

    traverse(root.left);

    minDiff = Math.min(minDiff, Math.abs(prev - root.val));
    prev = root.val;

    traverse(root.right);
  }
};
// @lc code=end

