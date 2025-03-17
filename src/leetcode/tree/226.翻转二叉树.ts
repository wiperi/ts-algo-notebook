/*
 * @lc app=leetcode.cn id=226 lang=typescript
 *
 * [226] 翻转二叉树
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

function invertTree(root: TreeNode | null): TreeNode | null {

  t(root);

  return root;
  

  function t(root: TreeNode) {
    if (root === null) return;
    if(root.left === null && root.right === null) return;

    
    t(root.left)
    t(root.right)
    
    let temp = root.right
    root.right = root.left
    root.left = temp
  }
};
// @lc code=end


export {}