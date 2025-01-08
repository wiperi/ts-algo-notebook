/*
 * @lc app=leetcode.cn id=101 lang=typescript
 *
 * [101] 对称二叉树
 */

import { BiTree, TreeNode } from '@/tree/BiTree';

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

function isSymmetric(root: TreeNode | null): boolean {
  let res = true;
  traverse(root, root);

  return res;

  function traverse(l: TreeNode, r: TreeNode) {

    if (res === false) return;

    if (l === null && r === null) return;

    if (Number(l === null) ^ Number(r === null) || l.val !== r.val) {
      res = false;
      return;
    }

    traverse(l.left, r.right);
    traverse(l.right, r.left);
  }
}
// @lc code=end

if (require.main === module) {
  let t = new BiTree([1, 2, 2, null, 3, null, 3]);
  console.log(isSymmetric(t.root));
}

export {}