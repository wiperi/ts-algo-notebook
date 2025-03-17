/*
 * @lc app=leetcode.cn id=226 lang=typescript
 *
 * [226] 翻转二叉树
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

function invertTree(root: TreeNode | null): TreeNode | null {

  if (root == null) {
    return null;
  }

  if (root.left || root.right) {
    let temp = root.left;
    root.left = root.right;
    root.right = temp;
  }
  
  root.left = invertTree(root.left);
  root.right = invertTree(root.right);

  return root;
}
// @lc code=end

(function invertTree(root: TreeNode | null): TreeNode | null {

  if (root == null) {
    return null;
  }
  
  root.left = invertTree(root.left);
  root.right = invertTree(root.right);

  if (root.left || root.right) {
    let temp = root.left;
    root.left = root.right
    root.right = temp;
  }

  return root;
})
