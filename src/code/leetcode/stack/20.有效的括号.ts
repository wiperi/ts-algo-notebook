/*
 * @lc app=leetcode.cn id=20 lang=typescript
 *
 * [20] 有效的括号
 */

// @lc code=start
function isValid(s: string): boolean {
  
  enum e {
    '(' = -3,
    '{' = -2,
    '[' = -1,
    ']' = 1,
    '}' = 2,
    ')' = 3,
  }

  let stack = [];


  for (let c of s) {
    if (e[c] < 0) {
      stack.push(e[c]);
    } else {
      if (-e[c] !== stack.pop()) return false;
    }
  }

  return stack.length === 0;
};
// @lc code=end

if (require.main === module) {
  console.log(isValid('([[][][]])'));
}

