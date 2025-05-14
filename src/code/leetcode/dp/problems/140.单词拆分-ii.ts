/*
 * @lc app=leetcode.cn id=140 lang=typescript
 *
 * [140] 单词拆分 II
 */

// @lc code=start
function wordBreak(s: string, wordDict: string[]): string[] {
  let path = [];
  let res: string[][] = [];

  dp(0);

  return res.flatMap(arr => arr.join(' '));

  function dp(start: number): void {
    if (start === s.length) {
      res.push(path.slice());
      return;
    } else if (start > s.length) {
      return;
    }

    for (let word of wordDict) {
      if (s.substring(start).indexOf(word) === 0) {
        path.push(word);
        dp(start + word.length);
        path.pop();
      }
    }

    return;
  }
}
// @lc code=end

export {};
