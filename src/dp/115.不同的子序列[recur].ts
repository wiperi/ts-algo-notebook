/*
 * @lc app=leetcode.cn id=115 lang=typescript
 *
 * [115] 不同的子序列
 */

// @lc code=start
function numDistinct(s: string, t: string) {
  // 从目标字符串的角度进行迭代
  // 对于 t[0] = 'r'，源字符串中所有的 'r' 都与一个可能的解决方案相关
  // 然后，对 t[1] 和 'r' 之后的源字符串子串进行相同的检查

  const memo = new Array(s.length).fill(0).map(() => new Array(t.length).fill(-1));
  return dp(0, 0);

  function dp(m: number, n: number) {
    if (n === t.length) return 1;

    if (s.length - m < t.length - n) return 0;

    if (memo[m][n] !== -1) return memo[m][n];

    let res = 0;
    for (let i = m; i < s.length; i++) {
      if (s.charAt(i) === t.charAt(n)) {
        res += dp(i + 1, n + 1);
      }
    }

    memo[m][n] = res;
    return res;
  }
}

// @lc code=end
