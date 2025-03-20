/*
 * @lc app=leetcode.cn id=15 lang=typescript
 *
 * [15] 三数之和
 */

// @lc code=start
function threeSum(nums: number[]): number[][] {
  // 顺序无关，子集类型问题
  // 输入有重复，元素不可复选

  // 状态：当前已选定了几个元素

  let path = [];
  let sum = 0;
  let res = [];

  nums.sort();
  backtrack(0);

  return res;


  function backtrack(start: number) {

    if (path.length === 3 && sum === 0) {
      res.push(path.slice())
      return;
    }

    let used = new Set();
    for (let i = start; i < nums.length; i++ ) {
      if (used.has(nums[i])) continue;
      used.add(nums[i]);

      path.push(nums[i]);
      sum += nums[i];
      backtrack(i + 1);
      sum -= nums[i];
      path.pop();
    }
  }
};
// @lc code=end

export {};