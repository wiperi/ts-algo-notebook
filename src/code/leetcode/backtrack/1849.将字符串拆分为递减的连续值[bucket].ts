/*
 * @lc app=leetcode.cn id=1849 lang=typescript
 *
 * [1849] 将字符串拆分为递减的连续值
 */

// @lc code=start
function splitString(s: string): boolean {
  // 选择：
  // 对于每个子串，它的长度可以是 1 to len(未被分割的部分) 
  // 状态：
  // 当前在选第几个字符

  let path = [];
  let res = false;
  
  backtrack(0, -1);

  return res;
  
  function backtrack(start: number, prev: number) {
    
    if (start === s.length) {
      if (path.length > 1) {
        res = true
      }
      return;
    }
 
    for (let end = start + 1; end <= s.length; end++) {
      let curr = Number(s.substring(start, end))
      if (prev !== -1 && (prev - curr) !== 1) continue;

      path.push(curr);
      backtrack(end, curr);
      if (res === true) return;
      path.pop();
    }
  }
}
// @lc code=end

if (require.main === module) {
  console.log(splitString("10009998")); // Output should be true or false based on the function logic
}
export {}