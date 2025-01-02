/*
 * @lc app=leetcode.cn id=931 lang=typescript
 *
 * [931] 下降路径最小和
 */
import _ from 'lodash';
// @lc code=start
function minFallingPathSum(matrix: number[][]): number {
  // state transition
  // input: [[a,b,c],[d,e,f],[g,h,i]]
  // f(b) = min(f(d), f(e), f(f)) + b

  // state: current starting position
  // choies: down below or diagonal left/right

  let [row, col] = [matrix.length, matrix[0].length];
  const MAX_VAL = Number.MAX_SAFE_INTEGER;
  let dp = _.times(row, () => Array(col).fill(MAX_VAL));
  dp[row - 1] = matrix[row - 1].slice();

  for (let r = row - 2; r >= 0; r--) {

    for (let c = 0; c < col; c++) {

      if (c === 0) {
        dp[r][c] = Math.min(dp[r + 1][c], dp[r + 1][c + 1]) + matrix[r][c];
      } else if (c === col - 1) {
        dp[r][c] = Math.min(dp[r + 1][c], dp[r + 1][c - 1]) + matrix[r][c];
      } else {
        dp[r][c] = Math.min(dp[r + 1][c], dp[r + 1][c - 1], dp[r + 1][c + 1]) + matrix[r][c];
      }
    }
  }

  return _.min(dp[0]);
}
// @lc code=end

if (require.main === module) {
  let res = minFallingPathSum([
    [2, 1, 3],
    [6, 5, 4],
    [7, 8, 9],
  ]);
  console.log(res);
}
