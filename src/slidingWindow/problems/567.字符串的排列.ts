/*
 * @lc app=leetcode.cn id=567 lang=typescript
 *
 * [567] 字符串的排列
 */

// @lc code=start
function checkInclusion(s1: string, s2: string): boolean {
  // 前提：一个合法窗口的长度 = s1的长度，所以使用定长窗口
  // 思路：维护2个频率统计表，和一个定长窗口，向右移动窗口，当2个频率表相等则返回真

  if (s1.length > s2.length) return false;

  let a = 'a'.charCodeAt(0)
  let win = Array(26).fill(0);
  let tar = Array(26).fill(0);

  // 初始化2个频率表
  for (let c of s1) {
    tar[code(c)] += 1; 
  }

  for (let c of s2.substring(0, s1.length)) {
    win[code(c)] += 1;
  }

  // 初始检测
  if (win.every((v, i) =>  v === tar[i])) return true;

  let left = 0, right = s1.length;
  while (right < s2.length) {
    // remove left
    win[code(s2[left])] -= 1;
    // add right
    win[code(s2[right])] += 1;

    if (win.every((v, i) =>  v === tar[i])) return true;

    left++;
    right++;
  }

  return false;


  function code(c: string) {
    if (c.length !== 1) throw 'input should be single char'
    return c.charCodeAt(0) - a;
  }
};
// @lc code=end

if (require.main === module) {
  console.log(checkInclusion('aab', 'kskbaa'))
}


export {}