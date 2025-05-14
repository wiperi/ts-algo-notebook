/*
 * @lc app=leetcode.cn id=70 lang=typescript
 *
 * [70] 爬楼梯
 */

// @lc code=start
function climbStairs(n: number): number {

  if (n <= 2) return n;

  let [a, b, res] = [1, 2, 0]

  for (let i = 3 ;i <= n; i++) {
    res = a + b;
    a = b
    b = res
  }

  return res;
}
// @lc code=end

if (require.main === module) {
  for (let i = 1; i < 10; i++) {
    let res = climbStairs(i);
    console.log(res);
  }
}

export {}