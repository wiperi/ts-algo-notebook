/*
 * @lc app=leetcode.cn id=115 lang=typescript
 *
 * [115] 不同的子序列
 */
import _ from 'lodash';
// @lc code=start
function numDistinct(s: string, t: string): number {
  // 从源字符串的角度进行迭代
  // 对于源字符串中的每个字符
  // 它有三种可能性
  // 1. 它匹配目标字符串，并且它在解中
  // 2. 它匹配目标字符串，但它不在解中
  // 3. 它不匹配目标字符串，当然它不在解中

  let memo = _.times(s.length, () => Array(t.length).fill(undefined));

  return dp(0, 0);

  function dp(m, n) {
    if (n == t.length) return 1;
    if (s.length - m < t.length - n) return 0;

    if (memo[m][n] !== undefined) return memo[m][n];

    let res = 0;
    if (s[m] === t[n]) {
      res = dp(m + 1, n + 1) + dp(m + 1, n);
    } else {
      res = dp(m + 1, n);
    }

    memo[m][n] = res;
    return memo[m][n];
  }
}
// @lc code=end
