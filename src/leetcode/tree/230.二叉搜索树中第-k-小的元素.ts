/*
 * @lc app=leetcode.cn id=230 lang=typescript
 *
 * [230] 二叉搜索树中第 K 小的元素
 */

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

function kthSmallest(root: TreeNode | null, k: number): number {

  let res = undefined;
  t(root);
  return res;

  function t(root) {

    if (res != undefined) {
      return;
    }


    if (root === null) return;

    t(root.left);

    k--;
    if (k == 0) {
      res = root.val;
      return;
    }

    t(root.right);
  }
};
// @lc code=end

