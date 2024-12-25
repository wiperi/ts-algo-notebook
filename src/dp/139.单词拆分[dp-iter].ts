/*
 * @lc app=leetcode.cn id=139 lang=typescript
 *
 * [139] 单词拆分
 */

// @lc code=start
function wordBreak(s: string, wordDict: string[]): boolean {
  // state: dp(x) means whether s[x..end] can be matched
  // choice: match which word in the wordDict
  // transition: dp(x) = dp(x + word.length) && s[x .. x + word.length] is in word, for word in dict

  let wordSet = new Set(wordDict);
  let memo = Array(s.length + 1).fill(-1);

  return dp(0);

  function dp(start: number): boolean {
    if (start === s.length) return true;

    if (memo[start] !== -1) return memo[start] === 1;

    for (let newStart = start + 1; newStart <= s.length; newStart++) {
      let substring = s.substring(start, newStart);

      if (wordSet.has(substring) && dp(newStart) === true) {
        memo[start] = 1;
        return true;
      }
    }

    memo[start] = 0;
    return false;
  }
}
// @lc code=end

if (require.main === module) {
  let res = wordBreak('leetcode', ['leet', 'code']);
  console.log(res);
}

export {};
