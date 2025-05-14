/*
 * @lc app=leetcode.cn id=526 lang=typescript
 *
 * [526] 优美的排列
 */

// @lc code=start
function countArrangement(n: number): number {

  let path = [undefined];
  let res = 0;

  backtrack();

  return res;

  function backtrack() {
    if (path.length - 1 === n) {
      res++;
      return;
    }
    
    
    for (let i = 1; i <= n; i++) {
      if (path.includes(i)) continue;
      if (path.length % i !== 0 && i % path.length !== 0) continue;
      
      path.push(i);
      backtrack();
      path.pop();
    }
  }
}
// @lc code=end

export {}