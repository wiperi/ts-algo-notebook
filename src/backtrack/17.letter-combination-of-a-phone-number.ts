/*
 * @lc app=leetcode.cn id=17 lang=typescript
 *
 * [17] 电话号码的字母组合
 */

// @lc code=start
function letterCombinations(digits: string): string[] {
  if (!digits) return [];

  let res: string[] = [];
  let path: string[] = [];
  let map: string[] = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz'];

  backtrack(0);
  return res;

  function backtrack(index: number) {
    if (path.length === digits.length) {
      res.push(path.join(''));
      return;
    }

    let str = map[parseInt(digits[index])];
    for (let i = 0; i < str.length; i++) {
      path.push(str[i]);
      backtrack(index + 1);
      path.pop();
    }
  }
}
// @lc code=end
