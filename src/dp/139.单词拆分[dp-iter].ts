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
  let memo = Array(s.length + 1).fill(null);

  return dp(0);

  function dp(start: number): boolean {
    if (start === s.length) return true;

    if (memo[start] !== null) return memo[start] === true;

    for (let newStart = start + 1; newStart <= s.length; newStart++) {
      let substring = s.substring(start, newStart);

      if (wordSet.has(substring) && dp(newStart) === true) {
        memo[start] = true;
        return true;
      }
    }

    memo[start] = false;
    return false;
  }
}
// @lc code=end

if (require.main === module) {
  let res = wordBreak('leetcode', ['leet', 'code']);
  console.log(res);
}

export {};
