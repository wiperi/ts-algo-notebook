/*
 * @lc app=leetcode.cn id=89 lang=typescript
 *
 * [89] 格雷编码
 */
import _ from 'lodash';
// @lc code=start
function grayCode(n: number): number[] {
  // choice: numbers that are one digit different to current number

  let path = [0];
  let used = Array(1 << n).fill(false)
  used[0] = true;
  let res = undefined;

  backtrack();

  return res;

  function backtrack() {
    if (path.length === 1 << n) {
      res = path;
      return;
    }

    for (let i = 0; i < n; i++) {
      let next = flipBit(_.last(path), i);
      if (used[next] === true) continue;

      used[next] = true;
      path.push(next);
      backtrack();
      if (res) return;
      path.pop();
      used[next] = false;
    }
  }
}

function flipBit(n: number, i: number) {
  return n ^ (1 << i);
}

// @lc code=end

if (require.main === module) {
  let res = grayCode(3);
  console.log(res);
}
