/*
 * @lc app=leetcode.cn id=77 lang=typescript
 *
 * [77] 组合
 */

// @lc code=start
function combine(n: number, k: number): number[][] {
  let res = [];
  let path = [];
  let nums = Array.from({ length: n }, (_, i) => i + 1);

  backtrack(0);

  return res;

  function backtrack(start) {
    if (path.length === k) {
      res.push(path.slice());
      return;
    }

    for (let [i, v] of nums.entries()) {
      if (i < start) continue;

      path.push(v);
      backtrack(i + 1);
      path.pop();
    }
  }
}
// @lc code=end

export {}