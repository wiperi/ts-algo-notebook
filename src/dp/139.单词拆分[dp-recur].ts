/*
 * @lc app=leetcode.cn id=139 lang=typescript
 *
 * [139] 单词拆分
 */

// @lc code=start
function wordBreak(s: string, wordDict: string[]): boolean {
  // state transition:
  // for input s == '123456789'
  // let f(x) be the result of s.substring(0, x)
  // if '789' matches in the dict, then check if '123456' also matched.
  // f(x) = f(x - word.length) and s[x - word.length .. x] is in word, for word in dict

  // memo[x] means whether s[0..x] can be matched
  let memo: number[] = Array(s.length + 1).fill(-1);
  let minLenOfWords = Number.MAX_SAFE_INTEGER;
  wordDict.forEach(w => {
    if (s.substring(0, w.length) === w) {
      memo[w.length] = 1;
    }
    minLenOfWords = Math.min(minLenOfWords, w.length);
  });

  return dp(s.length) === 1 ? true : false;

  function dp(end: number): number {
    if (end < minLenOfWords) {
      return 0;
    }

    if (memo[end] !== -1) return memo[end];

    let res = 0;
    for (let word of wordDict) {
      res = dp(end - word.length) && s.substring(end - word.length, end) === word ? 1 : 0;
      if (res === 1) break;
    }

    memo[end] = res;
    return memo[end];
  }
}
// @lc code=end

if (require.main === module) {
  let res = wordBreak('a', ['leet', 'a']);
  console.log(res);
}

export {};
