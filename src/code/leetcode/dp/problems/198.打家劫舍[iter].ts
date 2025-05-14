/*
 * @lc app=leetcode.cn id=198 lang=typescript
 *
 * [198] 打家劫舍
 */
import _ from 'lodash';
// @lc code=start
function rob(nums: number[]): number {
  // 状态：目前抢到第几家了
  // 选择：隔1家抢还是隔2家抢

  // 状态转移：
  // [a,b,c,d,e]
  // f(a) = nums[a]
  // f(b) = max(nums[a], nums[b])
  // f(e) = max(f(c), f(b)) + e

  if (nums.length === 1) return nums[0];

  let dp = Array(nums.length).fill(0);
  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for (let i = 2; i < dp.length; i++) {
    if (i - 3 >= 0) {
      dp[i] = Math.max(dp[i - 2], dp[i - 3]) + nums[i];
    } else {
      dp[i] = dp[i - 2] + nums[i];
    }
  }

  let n = nums.length;
  return Math.max(dp[n - 1], dp[n - 2]);
}
// @lc code=end

if (require.main === module) {
  let res = rob([2, 1, 1, 2]);
  console.log(res);
}

export {}