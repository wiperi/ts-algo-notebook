/*
 * @lc app=leetcode.cn id=784 lang=typescript
 *
 * [784] 字母大小写全排列
 */

// @lc code=start
function letterCasePermutation(s: string): string[] {
  // state: how many char left to process
  // choice: 
  // 2 choices

  let path = [];
  let res: string[][] = [];

  backtrack(0);

  return res.map(v => v.join(''));

  function backtrack(i: number) {
    if (path.length === s.length) {
      res.push(path.slice());
      return;
    };

    if (/\d/.test(s[i])) {
      path.push(s[i]);
      backtrack(i + 1);
      path.pop();
      return;
    }

    path.push(s[i].toUpperCase());
    backtrack(i + 1);
    path.pop();
    
    path.push(s[i].toLowerCase());
    backtrack(i + 1);
    path.pop();
  }
};
// @lc code=end


export {}