/*
 * @lc app=leetcode.cn id=72 lang=typescript
 *
 * [72] 编辑距离
 */

// @lc code=start
function minDistance(s1: string, s2: string): number {
  let memo: number[][] = [];
  let m = s1.length, n = s2.length;
  // 备忘录初始化为特殊值，代表还未计算
  for (let i = 0; i <= m; i++) {
      memo[i] = new Array(n + 1).fill(-1);
  }
  return dp(m - 1, n - 1);
  
  // 返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
  function dp(i: number, j: number): number {
    if (i == -1) return j + 1;
    if (j == -1) return i + 1;
    // 查备忘录，避免重叠子问题
    if (memo[i][j] != -1) {
      return memo[i][j];
    }
    // 状态转移，结果存入备忘录
    if (s1.charAt(i) == s2.charAt(j)) {
      memo[i][j] = dp(i - 1, j - 1);
    } else {
      memo[i][j] = Math.min(
        dp(i, j - 1) + 1,
        dp(i - 1, j) + 1,
        dp(i - 1, j - 1) + 1
      );
    }
    return memo[i][j];
  }
}
// @lc code=end

export {};

