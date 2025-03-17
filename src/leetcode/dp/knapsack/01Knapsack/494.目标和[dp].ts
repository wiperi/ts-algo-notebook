/*
 * @lc app=leetcode.cn id=494 lang=typescript
 *
 * [494] 目标和
 */

// @lc code=start
function findTargetSumWays(nums: number[], target: number): number {
  let memo = new Map();
  return dp(0, target);

  function dp(i, remain) {
    let key = `${i},${remain}`;

    if (i === nums.length && remain === 0) {
      return 1;
    }

    if (i === nums.length) {
      return 0;
    }

    if (memo.has(key)) return memo.get(key);

    // 2 options: + or -
    let res = dp(i + 1, remain - nums[i]) + dp(i + 1, remain + nums[i]);
    memo.set(key, res);
    return res;
  }
}
// @lc code=end

// dp version without memo
(function findTargetSumWays(nums: number[], target: number): number {
  return dp(0, target);

  function dp(i, remain) {
    if (i === nums.length && remain === 0) {
      return 1;
    }

    if (i === nums.length) {
      return 0;
    }

    // 2 options: + or -
    return dp(i + 1, remain - nums[i]) + dp(i + 1, remain + nums[i]);
  }
});

export {};
