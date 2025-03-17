/*
 * @lc app=leetcode.cn id=354 lang=typescript
 *
 * [354] 俄罗斯套娃信封问题
 */

import _ from 'lodash';

// @lc code=start
function maxEnvelopes(envelopes: number[][]): number {
    // 按宽度升序排列，如果宽度一样，则按高度降序排列
    let n = envelopes.length;
    envelopes.sort((a, b) => a[0] != b[0] ? a[0] - b[0] : b[1] - a[1]);
    // 对高度数组寻找 LIS
    let height = new Array(n);
    for (let i = 0; i < n; i++)
        height[i] = envelopes[i][1];

    return lengthOfLIS(height);
}

function lengthOfLIS(nums: number[]): number {
  // dp[n] = 对于长度为n的LIS，它的末尾数字的最小值
  let dp: number[] = [];

  for (let num of nums) {
    // 使用 biSearch 找到第一个 >= num 的位置
    let pos = biSearch(dp, num);
    if (pos === dp.length) {
      dp.push(num); // 如果 num 比 dp 中所有值都大，追加
    } else {
      dp[pos] = num; // 替换掉第一个 >= num 的值
    }
  }

  return dp.length; // 返回 dp 的长度，即最长递增子序列的长度
}

function biSearch(arr: number[], target: number): number {
  let left = 0,
    right = arr.length;
  while (left < right) {
    let mid = Math.floor((left + right) / 2);
    if (arr[mid] < target) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left;
}
// @lc code=end

export {}