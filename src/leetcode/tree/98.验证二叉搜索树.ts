/*
 * @lc app=leetcode.cn id=98 lang=typescript
 *
 * [98] 验证二叉搜索树
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

function isValidBST(root: TreeNode | null): boolean {
  let res = true;

  t(root, -Infinity, Infinity);

  return res;

  function t(root, min, max) {
    if (root == null) return;

    if (res === false) return;

    if (root.val <= min || root.val >= max) {
      res = false;
      return;
    }

    t(root.left, min, root.val);
    t(root.right, root.val, max);

    return;
  }
}
// @lc code=end
