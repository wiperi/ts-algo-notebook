/*
 * @lc app=leetcode.cn id=698 lang=typescript
 *
 * [698] 划分为k个相等的子集
 */
import _ from 'lodash'
// @lc code=start
function canPartitionKSubsets(nums: number[], k: number): boolean {

  // 站在桶的角度遍历
  // 状态：已经装了几个桶
  // 选择：每个没被用过的元素都有机会装入当前桶

  if (k > nums.length ) return false;
  let sum = _.sum(nums);
  if (sum % k !== 0) return false;

  let target = sum / k;

  let used = Array(nums.length).fill(false);
  let res = false;

  backtrack(0, 0, 0);

  return res;

  // nthBuc 已经装满了几个桶
  // bucSum 当前桶的sum
  function backtrack(start, nthBuc, bucSum) {

    // 已经装满 k 个桶，结束计算
    if(nthBuc === k) {
      res = true;
      return;
    }

    // 当前桶装满了，装下一个桶
    if (bucSum === target) {
      backtrack(0, nthBuc + 1, 0);
      return;
    }

    for (let i = start; i < nums.length; i++) {
      // 元素不可重复使用
      if (used[i] === true) continue;
      // 当前桶将要溢出
      if (bucSum + nums[i] > target) continue;

      used[i] = true;
      backtrack(i + 1, nthBuc, bucSum + nums[i]);
      if (res === true) return;
      used[i] = false;
    }
  }
};
// @lc code=end

