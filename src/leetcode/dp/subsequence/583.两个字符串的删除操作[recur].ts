/*
 * @lc app=leetcode.cn id=583 lang=typescript
 *
 * [583] 两个字符串的删除操作
 */

// @lc code=start
function minDistance(s1: string, s2: string): number {
  // let f(i, j) = minDistance(s1[i..end], s2[j..end])
  // assume f(i, j) known
  // for i - 1, j - 1
  // there are 3 options: delete s1[i - 1] or delete s1[j - 1] or do nothing

  let memo = Array.from({ length: s1.length + 1 }).map(() =>
    Array.from({ length: s2.length + 1 }).fill(-1)
  );

  return dp(s1.length - 1, s2.length - 1);

  function dp(i, j) {
    let [m, n] = [i + 1, j + 1];

    if (memo[m][n] !== -1) return memo[m][n];

    if (i < 0) {
      memo[m][n] = j + 1;
      return j + 1;
    }
    if (j < 0) {
      memo[m][n] = i + 1;
      return i + 1;
    }

    if (s1[i] === s2[j]) {
      memo[m][n] = dp(i - 1, j - 1);
    } else {
      memo[m][n] = Math.min(dp(i, j - 1), dp(i - 1, j)) + 1;
    }

    return memo[m][n];
  }
}
// @lc code=end

if (require.main === module) {
  let res = minDistance('saa', 'aab');
  console.log(res);
}

(function minDistance(s1: string, s2: string): number {
  // let f(i, j) = minDistance(s1[i..], s2[j..])
  // assume f(i, j) known
  // for i - 1, j - 1
  // there are 3 options: delete s1[i - 1] or delete s1[j - 1] or do nothing

  return dp(s1.length - 1, s2.length - 1);

  function dp(i, j) {
    if (i < 0) {
      return j + 1;
    }
    if (j < 0) {
      return i + 1;
    }

    if (s1[i] === s2[j]) {
      return dp(i - 1, j - 1);
    } else {
      return Math.min(dp(i, j - 1), dp(i - 1, j)) + 1;
    }
  }
});

export {}