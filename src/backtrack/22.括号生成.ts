/*
 * @lc app=leetcode.cn id=22 lang=typescript
 *
 * [22] 括号生成
 */

// @lc code=start
function generateParenthesis(n: number): string[] {

  let path = [];
  // 左括号剩余数量，右括号剩余数量
  let [left, right] = [n, n];
  let res = [];

  backtrack();

  let resStr = [];
  res.forEach(path => {
    let str = path.map(v => (v === 1 ? '(' : ')')).join('');
    resStr.push(str);
  });

  return resStr;

  function backtrack() {
    // 左右括号都用完了，得到一个合法的括号组合
    if (left === 0 && right === 0) {
      res.push(path.slice());
      return;
    }

    for (let choice of [1, -1]) {
      // 左括号剩余数量小于 0 或者右括号剩余数量小于 0，跳过
      if (left < 0 || right < 0) continue;
      // 确保左括号剩余数量 <= 右括号剩余数量，即，使用右括号前，必须有左括号
      if (right < left) continue;

      left -= choice === 1 ? 1 : 0;
      right -= choice === -1 ? 1 : 0;
      path.push(choice);
      backtrack();
      path.pop();
      left += choice === 1 ? 1 : 0;
      right += choice === -1 ? 1 : 0;
    }
  }
}
// @lc code=end
