/*
 * @lc app=leetcode.cn id=139 lang=typescript
 *
 * [139] 单词拆分
 */

// @lc code=start
function wordBreak(s: string, wordDict: string[]): boolean {
 
  // let f(0) = wordBreak(s[0..end])
  
  // state transition:
  // f(0) = (s[0..] match the word) && f(word.length) for word in wordDict

  let memo: Array<boolean | null> = Array(s.length + 1).fill(null);

  return dp(0);

  function dp(start) {

    if (memo[start] !== null) return memo[start];

    if (start === s.length) {
      memo[start] = true;
      return true;
    } else if (start > s.length) {
      memo[start] = false;
      return false;
    }

    let res = false;
    for (let word of wordDict) {
      if (s.substring(start).indexOf(word) === 0) {
        res = dp(start + word.length) || res;
        memo[start] = res;
      }
    }

    return res;
  }
};
// @lc code=end

(function wordBreak(s: string, wordDict: string[]): boolean {
 
  // let f(0) = wordBreak(s[0..end])
  
  // state transition:
  // f(0) = (s[0..] match the word) && f(word.length) for word in wordDict

  return dp(0);

  function dp(start) {

    if (start === s.length) {
      return true;
    } else if (start > s.length) {
      return false;
    }

    let res = false;
    for (let word of wordDict) {
      if (s.substring(start).indexOf(word) === 0) {
        res = dp(start + word.length) || res;
      }
    }

    return res;
  }
});
