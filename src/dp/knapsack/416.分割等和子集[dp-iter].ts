/*
 * @lc app=leetcode.cn id=416 lang=typescript
 *
 * [416] 分割等和子集
 */
import _ from 'lodash'
// @lc code=start
function canPartition(nums: number[]): boolean {
  // 问题：能否分出一个承重量 sum / 2 的背包，正好将其装满

  let sum = _.sum(nums)
  if (sum % 2 !== 0) return false;
  
  // dp[i][j] = 对于前 i 个item，称重量为 j 的背包，能否装下
  let dp = _.times(nums.length + 1, () => Array(sum / 2 + 1).fill(false))

  // 当承重量为0的时候，总是可以装满背包的
  for (let i = 0; i < nums.length + 1; i++) {
    dp[i][0] = true;
  }

  for (let i = 1; i < nums.length + 1; i++) {
    for (let j = 0 ;j <= sum / 2; j++) {
      let weight = nums[i - 1];

      // 背包承重量不足
      if (j < weight) {
        dp[i][j] = dp[i - 1][j];
        continue;
      }
      
      // 放入当前物品 or 不放入当前物品
      dp[i][j] = dp[i - 1][j - weight] || dp[i - 1][j];
    }
  }

  return dp[nums.length][sum / 2]
}
// @lc code=end

export {}