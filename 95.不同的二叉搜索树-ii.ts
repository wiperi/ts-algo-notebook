/*
 * @lc app=leetcode.cn id=95 lang=typescript
 *
 * [95] 不同的二叉搜索树 II
 */

import { TreeNode } from "@/adt/BiTree";
import { BST, BSTNode } from "data-structure-typed";
import { BinarySearchTree } from "datastructures-js";

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

function generateTrees(n: number): Array<TreeNode | null> {

  // Build a array from 1 to n.
  let permutatons: number[][] = perm(n);
  
  // Generate bst based on the permutaton of array.

  const res = [];

  for (let i = 0; i < permutatons.length; i++) {

    const bst = new BST<number>();
    permutatons[i].forEach(v => {
      bst.add(v);
    })
    bst.print();

    res.push(getLevel(bst.root));
  }

  return res;
};

function getLevel(root: BSTNode) {
  const q = [root];
  const res = [];

  while (q.length != 0 ) {
    const curr = q.shift();
    res.push(curr ? curr.key : null);
    
    if (!curr) continue;

    q.push(curr.left);
    q.push(curr.right);
  }

  return res;
}

function perm(n) {

  // State: How many number are choosed
  
  const res = [];
  const path = [];
  const visited = Array(n).fill(false);
  backTrack(0);

  return res;
  

  function backTrack(numChoosed) {
    if (numChoosed === n) {
      res.push([...path]);
      return;
    }

    for (let i = 1; i <= n; i++) {
      if (visited[i] === true) continue;

      path.push(i);
      visited[i] = true;
      backTrack(numChoosed + 1);
      visited[i] = false;
      path.pop();
    }
  }
}
// @lc code=end

if (require.main === module) {
  console.log(generateTrees(3));
}

