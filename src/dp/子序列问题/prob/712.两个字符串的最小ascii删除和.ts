import _ from 'lodash';

/*
 * @lc app=leetcode.cn id=712 lang=typescript
 *
 * [712] 两个字符串的最小ASCII删除和
 */

// @lc code=start
function minimumDeleteSum(s1: string, s2: string): number {
  // leetcode 583 两个字符串的删除操作 的变体

  let memo = _.times(s1.length, () => Array(s2.length).fill(-1));

  return dp(s1.length - 1, s2.length - 1);

  function dp(i, j) {

    if (i < 0) {
      return _.sumBy(s2.slice(0, j + 1), char => char.charCodeAt(0));
    }

    if (j < 0) {
      return _.sumBy(s1.slice(0, i + 1), char => char.charCodeAt(0));
    }

    if (memo[i][j] !== -1) return memo[i][j];

    if (s1[i] === s2[j]) {
      memo[i][j] = dp(i - 1, j - 1);
    } else {
      memo[i][j] = Math.min(dp(i, j - 1) + s2.charCodeAt(j), dp(i - 1, j) + s1.charCodeAt(i));
    }

    return memo[i][j];
  }
}
// @lc code=end

if (require.main === module) {
  console.log(Array.from('123'));
}

(function minimumDeleteSum(s1: string, s2: string): number {
  return dp(s1.length - 1, s2.length - 1);

  function dp(i, j) {
    if (i < 0) {
      return _.sumBy(s2.slice(0, j + 1), char => char.charCodeAt(0));
    }

    if (j < 0) {
      return _.sumBy(s1.slice(0, i + 1), char => char.charCodeAt(0));
    }

    if (s1[i] === s2[j]) {
      return dp(i - 1, j - 1);
    } else {
      return Math.min(dp(i, j - 1) + s2.charCodeAt(j), dp(i - 1, j) + s1.charCodeAt(i));
    }
  }
});
