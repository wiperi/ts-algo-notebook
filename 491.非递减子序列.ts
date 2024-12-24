/*
 * @lc app=leetcode.cn id=491 lang=typescript
 *
 * [491] 非递减子序列
 */
import _ from 'lodash'
// @lc code=start
function findSubsequences(nums: number[]): number[][] {

  let path: number[] = [];
  let res = [];

  backtrack(0);

  return res;
  
  function backtrack(start) {

    if (path.length >= 2) {
      res.push(path.slice());
    }

    let used = new Set();
    for (let i = start; i < nums.length; i++) {
      if (used.has(nums[i])) continue;
      if (path.length > 0 && _.last(path) > nums[i]) continue;

      used.add(nums[i]);
      path.push(nums[i]);
      backtrack(i + 1);
      path.pop();
    }
  }
}
// @lc code=end

if (require.main === module) {
  let res = findSubsequences([4,6,7,7])
  console.log(res);
}