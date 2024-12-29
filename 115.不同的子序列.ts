/*
 * @lc app=leetcode.cn id=115 lang=typescript
 *
 * [115] 不同的子序列
 */

// @lc code=start
function numDistinct(s: string, t: string): number {
  // state transition:
  // let f(i, j) be, matching t[j..end] in s[i..end]

  let res = 0;
  let memo = _.times(s.length + 1, () => Array(t.length + 1).fill(-1));

  dp(0, 0);

  return res;



  function dp(i, j) {
    
    if (memo[i][j] !== -1) return;
    
    if (j == t.length) {
      res++;
      memo[i][j] = res;
      return;
    }
    
    if (i >= s.length) {
      memo[i][j] = 0;
      return;
    }

    for (let k = i; k < s.length; k++) {
      if (s[k] !== t[j]) continue;

      dp(k + 1, j + 1);
    }
  }
};
// @lc code=end

