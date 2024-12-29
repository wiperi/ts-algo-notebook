/*
 * @lc app=leetcode.cn id=698 lang=typescript
 *
 * [698] 划分为k个相等的子集
 */
// @lc code=start
function canPartitionKSubsets(nums: number[], k: number) {
  // 排除一些基本情况
  if (k > nums.length) return false;
  let sum = nums.reduce((a, b) => a + b, 0);

  // target 不是整数，直接返回 false
  if (sum % k !== 0) return false;

  const target = sum / k;
  const len = nums.length;
  // 使用位图表示哪些数字已被使用，初始为 0
  let used = 0;
  // 记录已经尝试过的 used 状态
  const memo = new Set<number>();
  let res = false;

  // 排序数组，大的数字在前面，更快触发剪枝逻辑
  nums.sort((a, b) => b - a);

  // 最大的数比目标值还大，直接返回 false
  if (nums[0] > target) return false;

  backtrack(k, 0, 0);

  return res;

  function backtrack(numBucLeft, bucketSum, start) {
    // 所有桶已被装满，由于剪枝逻辑，此时每个桶的sum必然 == target
    if (numBucLeft === 0) {
      res = true;
      return;
    }

    if (bucketSum === target) {
      // 当前桶装满了，装下一个桶
      backtrack(numBucLeft - 1, 0, 0);
      return;
    }

    // 如果当前状态已经计算过，直接返回
    if (memo.has(used)) return;
    memo.add(used);

    // 选择空间：对于每个桶，遍历每个数字
    for (let i = start; i < len; i++) {

      // 如果 nums[i] 已经被用，跳过
      if (((used >> i) & 1) === 1) continue;

      // 当前桶装不下 nums[i]
      if (nums[i] + bucketSum > target) continue;

      used |= 1 << i;
      bucketSum += nums[i];

      // 递归穷举下一个数字是否装入当前桶
      backtrack(numBucLeft, bucketSum, i + 1);
      if (res === true) return;

      used &= ~(1 << i);
      bucketSum -= nums[i];
    }
  }
}

// @lc code=end

export {};