/*
 * @lc app=leetcode.cn id=72 lang=typescript
 *
 * [72] 编辑距离
 */

// @lc code=start
function minDistance(s1: string, s2: string): number {
  let m = s1.length, n = s2.length;
  // i，j 初始化指向最后一个索引
  return dp(m - 1, n - 1);
  
  // 定义：返回 s1[0..i] 和 s2[0..j] 的最小编辑距离
  function dp(i: number, j: number): number {
    // base case
    if (i == -1) return j + 1;
    if (j == -1) return i + 1;
    
    if (s1.charAt(i) == s2.charAt(j)) {
      // 啥都不做
      return dp(i - 1, j - 1);
    }
    return Math.min(
      // 插入
      dp(i, j - 1) + 1,
      // 删除
      dp(i - 1, j) + 1,
      // 替换
      dp(i - 1, j - 1) + 1,
    );
  }
}
  // @lc code=end

export {};

