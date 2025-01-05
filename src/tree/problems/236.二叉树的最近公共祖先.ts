/*
 * @lc app=leetcode.cn id=236 lang=typescript
 *
 * [236] 二叉树的最近公共祖先
 */

import { TreeNode } from '@/tree/BiTreeGeneric';

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

function lowestCommonAncestor(
  root: TreeNode | null,
  p: TreeNode | null,
  q: TreeNode | null
): TreeNode | null {

  // 思路：
  // 对于一个3节点的二叉树
  // function problem(root) {
  //   if (root === null || root === p || root === q) return root;
  //   let left = problem(root.left);
  //   let right = problem(root.right);
  //   if (left && right) return root;

  //   if (left && !right) {
  //   } // LCS is not root, is in left subtrees
  //   if (!left && right) {
  //   } // LCS is not root, is in right subtrees
  // }

  let found = false;
  
  return lcs(root);

  function lcs(root: TreeNode) {
    if (root === null) return root;
    if (found === true) return null;

    if (root === p || root === q) return root;

    let left = lcs(root.left);
    let right = lcs(root.right)

    if (left === null && right === null) return null;
    else if (left === null) return right;
    else if (right === null) return left;
    else {
      found = true;
      return root;
    }
  }
}
// @lc code=end

export {}