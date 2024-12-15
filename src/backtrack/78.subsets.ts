/*
 * @lc app=leetcode.cn id=78 lang=typescript
 *
 * [78] 子集
 */

// @lc code=start
function subsets(nums: number[]): number[][] {
  let res = [];
  let path = [];

  backtrack(0);

  return res;

  function backtrack(start) {
    res.push(path.slice());

    for (let [i, v] of nums.entries()) {
      if (i < start) continue;

      path.push(v);
      backtrack(i + 1);
      path.pop();
    }
  }
}
// @lc code=end
