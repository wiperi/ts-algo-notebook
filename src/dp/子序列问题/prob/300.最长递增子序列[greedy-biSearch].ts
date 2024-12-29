/*
 * @lc app=leetcode.cn id=300 lang=typescript
 *
 * [300] 最长递增子序列
 */

import _ from 'lodash';

// @lc code=start
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

if (require.main === module) {
  let res = lengthOfLIS([10, 9, 2, 5, 3, 0, 7, 11, 101, 18]);
  console.log(res);
}
