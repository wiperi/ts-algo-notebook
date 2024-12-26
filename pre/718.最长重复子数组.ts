/*
 * @lc app=leetcode.cn id=718 lang=typescript
 *
 * [718] 最长重复子数组
 */

// @lc code=start
function findLength(nums1: number[], nums2: number[]): number {
  const n = nums1.length;
  const m = nums2.length;

  // dp[i][j] = nums1[i..end] and nums2[j..end] 的最大公共子数组距离
  const dp: number[][] = Array.from({ length: n + 1 }, () => Array(m + 1).fill(0));
  let ans = 0;

  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) {
      if (nums1[i] === nums2[j]) {
        dp[i][j] = dp[i + 1][j + 1] + 1;
      } else {
        dp[i][j] = 0;
      }
      ans = Math.max(ans, dp[i][j]);
    }
  }

  return ans;
}
// @lc code=end
