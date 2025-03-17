/*
 * @lc app=leetcode.cn id=93 lang=typescript
 *
 * [93] 复原 IP 地址
 */

// @lc code=start
function restoreIpAddresses(s: string): string[] {
  // problem: separate the string to 4 parts, each parts has to meet some rule
  // state: how many digits are settled
  // choice: how to separate next partition

  let parts = [];
  let res: string[][] = [];
  
  backtrack(0, 0);

  return res.map(arr => arr.join('.'))

  function backtrack(start, depth) {

    if (start === s.length) {
      res.push(parts.slice());
      return
    }


    for (let i = 1; i <= 3; i++) {
      let newPart = s.substring(start, start + i);

      // leading 0 case
      if (newPart[0] === '0' && newPart.length > 1) continue;

      // each parts should not larger then 255
      if (Number(newPart) > 255) continue;
      
      // we will run out of digits, but haven't divided the string to 4 parts yet. 
      if (start + i >= s.length && depth + 1 !== 4) continue;

      parts.push(newPart);
      backtrack(start + i, depth + 1);
      parts.pop();
    }

  }
};
// @lc code=end

if (require.main === module) {
  let res = restoreIpAddresses('19999')
  console.log(res);
}
export {}