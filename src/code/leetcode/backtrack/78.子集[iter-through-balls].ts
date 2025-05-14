/*
 * @lc app=leetcode.cn id=78 lang=typescript
 *
 * [78] 子集
 */

import { BiTree, TreeNode } from "@/adt/BiTree";

// @lc code=start
let t = new BiTree(['root']);
function subsets(nums: number[]): number[][] {
  let res = [];
  let path = [];

  backtrack(0, t.root);

  return res;

  /**
   * @param done 已经完成选择的球的个数
   */
  function backtrack(done, root: TreeNode) {
    if (done === nums.length) {
      res.push(path.slice());
      return;
    }

    // 球盒模型，站在球的角度遍历
    // 对于每个球（nums中的数字），选择空间为[放入盒中，不放入]
    root.left = new TreeNode(nums[done])
    path.push(nums[done]);
    backtrack(done + 1, root.left);
    path.pop();

    root.right = new TreeNode('_');
    backtrack(done + 1, root.right);
  }
}
// @lc code=end

if (require.main === module) {
  subsets([1, 2, 3]);
  console.log(t);
}

export {}