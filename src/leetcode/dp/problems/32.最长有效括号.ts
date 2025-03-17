/*
 * @lc app=leetcode.cn id=32 lang=typescript
 *
 * [32] 最长有效括号
 */

// @lc code=start
function longestValidParentheses(s: string): number {
  if (s.length == 0) return 0;

  // state: len of s
  // state transition:
  // if (s[i] is valid right paren) {
  //   get the current valid length;
  //   f(0..i) = current valid length + f(0..i - 1);
  // }

  // dp[i] = f(s[0..i]), for any s[i] == ')'
  // since, if s[i] == '(', no need to record answer for s[i]
  let dp = Array(s.length).fill(0);

  // record last left paren index
  let st = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') {
      st.push(i);
      dp[i] = 0;
    } else if (s[i] === ')') {
      if (st.length === 0) {
        dp[i] = 0;
      } else if (st.length != 0) {
        let leftIndex = st.pop();
        let len = i - leftIndex + 1 + (dp[leftIndex - 1] ?? 0);
        dp[i] = len;
      }
    }
  }

  return _.max(dp);
}
// @lc code=end
