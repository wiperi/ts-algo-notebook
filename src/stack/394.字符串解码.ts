/*
 * @lc app=leetcode.cn id=394 lang=typescript
 *
 * [394] 字符串解码
 */

// @lc code=start
function decodeString(s: string): string {
  let stack: [number, string][] = [];
  let res = '';
  let multi = 0;

  for (let char of s) {

    if (char === '[') {
      stack.push([multi, res]);
      res = '';
      multi = 0;
      continue;
    }

    if (char === ']') {
      let [currentMulti, lastRes] = stack.pop()!;
      res = lastRes + res.repeat(currentMulti);
      continue;
    }

    if (/\d/.test(char)) {
      multi = multi * 10 + Number(char);
      continue;
    }

    res += char;
  }

  return res;
}
// @lc code=end

if (require.main === module) {
  console.log(decodeString('3[a2[c]]'));
}

export {}