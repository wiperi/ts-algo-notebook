/*
 * @lc app=leetcode.cn id=46 lang=typescript
 *
 * [46] 全排列
 */

// @lc code=start
function permute(nums: number[]): number[][] {
  let res = [];
  let path = [];

  backtrack();

  return res;

  function backtrack() {
    
    if (path.length === nums.length) {
      res.push(path.slice());
      return;
    }

    for (let [i, v] of nums.entries()) {
      if (path.includes(v)) continue;

      path.push(v);
      backtrack();
      path.pop();
    }
  }
}
// @lc code=end

export {}