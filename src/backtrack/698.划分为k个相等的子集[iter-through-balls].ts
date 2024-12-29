/*
 * @lc app=leetcode.cn id=698 lang=typescript
 *
 * [698] 划分为k个相等的子集
 */
import _ from 'lodash';
// @lc code=start
function canPartitionKSubsets(nums: number[], k: number): boolean {
  // 站在元素的角度遍历
  // 选择：每个元素都有机会去到k个桶中的一个
  // 状态：当前遍历到了第几个元素

  if (k > nums.length) return false;
  let sum = _.sum(nums);
  if (sum % k !== 0) return false;

  let target = sum / k;

  // res: -1 = undefined, 0 = false, 1 = true
  let res = -1;

  // sum of each buckets
  let buckets = Array(k).fill(0);

  backtrack(0);

  return res === 1;

  function backtrack(index) {
    
    // 遍历了所有元素
    if (index === nums.length) {
      // 由于剪枝逻辑，此时每个 sum of each buckets can only <= target
      if (buckets.every(b => b === target)) {
        res = 1;
      } else {
        res = 0;
      }

      return;
    }

    for (let i = 0; i < buckets.length; i++) {
      // 桶即将溢出，剪枝
      if (buckets[i] + nums[index] > target) continue;

      buckets[i] += nums[index];
      backtrack(index + 1);
      if (res !== -1) return;
      buckets[i] -= nums[index];
    }
  }
}
// @lc code=end
