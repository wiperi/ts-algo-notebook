/*
 * @lc app=leetcode.cn id=416 lang=typescript
 *
 * [416] 分割等和子集
 */
import _ from 'lodash';
// @lc code=start
function canPartition(nums: number[]): boolean {
  
  // 空间压缩

  // 问题：能否分出一个承重量 sum / 2 的背包，正好将其装满

  let sum = _.sum(nums)
  if (sum % 2 !== 0) return false;
  
  // dp[i][j] = 对于前 i 个item，称重量为 j 的背包，能否装下
  let dp = Array(sum / 2 + 1).fill(false);

  // 当承重量为0的时候，总是可以装满背包的
  dp[0] = true;

  for (let i = 1; i < nums.length + 1; i++) {
    for (let j = sum / 2 ;j >= 0; j--) {
      let weight = nums[i - 1];

      if (j < weight) {
        continue;
      }
      
      // 放入当前物品 or 不放入当前物品
      dp[j] = dp[j - weight] || dp[j]
    }
  }

  return dp[sum / 2];
}
// @lc code=end


export {}