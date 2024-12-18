/*
 * @lc app=leetcode.cn id=131 lang=typescript
 *
 * [131] 分割回文串
 */

// @lc code=start
function partition(s: string): string[][] {
  let res = [];
  let path = [];

  backtrack(s);

  return res;

  /**
   * @param str 当前节点的选择空间
   */
  function backtrack(str: string) {
    
    if (str.length === 0) {
      // 所有字符已用完，且路径上每个串都是回文串
      res.push(path.slice());
      return;
    }

    for (let i = 1; i <= str.length; i++) {
      let sub = str.substring(0, i);

      // 确保路径上每个选择（字串）都是回文串
      if (!isPalindrome(sub)) continue;

      path.push(sub);
      // 缩小下一层节点的选择空间
      backtrack(str.substring(i, str.length));
      path.pop();
    }
  }
}

function isPalindrome(str: string) {
  let [l, r] = [0, str.length - 1];

  while (l < r) {
    if (str[l] !== str[r]) return false;

    l++;
    r--;
  }

  return true;
}
// @lc code=end

if (require.main === module) {
  partition('aab');
}

export {};
