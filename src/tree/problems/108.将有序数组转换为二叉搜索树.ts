/*
 * @lc app=leetcode.cn id=108 lang=typescript
 *
 * [108] 将有序数组转换为二叉搜索树
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

function sortedArrayToBST(nums: number[]): TreeNode | null {
  
  return build(0, nums.length - 1);

  function build(left: number, right: number) {

    if ((left <= right) === false) {
      return null;
    }

    let mid = Math.floor((left + right) / 2)

    let root = new TreeNode(nums[mid])

    root.left = build(left, mid - 1);
    root.right = build(mid + 1, right);

    return root;
  }

};
// @lc code=end

export {}