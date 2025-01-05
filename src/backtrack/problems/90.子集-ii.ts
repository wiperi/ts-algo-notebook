/*
 * @lc app=leetcode.cn id=90 lang=typescript
 *
 * [90] 子集 II
 */

// @lc code=start
function subsetsWithDup(nums: number[]): number[][] {
  let path = [];
  let res = [];

  nums.sort();
  backtrack(0);

  return res;

  function backtrack(start: number) {
    console.log(path);

    res.push(path.slice());

    let used = new Set();

    for (let i = start; i < nums.length; i++) {
      if (used.has(nums[i])) continue;
      used.add(nums[i]);

      path.push(nums[i]);
      backtrack(i + 1);
      path.pop();
    }
  }
}
// @lc code=end

export {}