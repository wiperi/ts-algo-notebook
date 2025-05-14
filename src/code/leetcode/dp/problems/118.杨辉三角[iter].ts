/*
 * @lc app=leetcode.cn id=118 lang=typescript
 *
 * [118] 杨辉三角
 */

// @lc code=start
function generate(numRows: number): number[][] {

  // 对于每一层，两边都是1，用上一层的数字计算本层的中间部分

  let dp = [undefined, [1]];

  for (let i = 2; i <= numRows; i++) {
    dp[i] = [1];

    for (let [l, r] = [0, 1]; r < i - 1; l++,r++) {
      dp[i].push(dp[i - 1][l] + dp[i - 1][r]);
    }

    dp[i].push(1);
  }

  dp.shift();
  return dp;
}
// @lc code=end

export {}