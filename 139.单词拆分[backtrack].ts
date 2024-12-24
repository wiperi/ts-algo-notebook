/*
 * @lc app=leetcode.cn id=139 lang=typescript
 *
 * [139] 单词拆分
 */

// @lc code=start
function wordBreak(s: string, wordDict: string[]): boolean {
  // state: how many char has already been matched
  // choice: match which word in the wordDict

  let res = false;

  backtrack(0);

  return res;

  function backtrack(start: number) {
    if (start === s.length) {
      res = true;
      return;
    }

    for (let word of wordDict) {
      if (s.substring(start).indexOf(word) !== 0) continue;

      backtrack(start + word.length);
      if (res === true) return;
    }
  }
}
// @lc code=end

export {};
