/*
 * @lc app=leetcode.cn id=5 lang=typescript
 *
 * [5] 最长回文子串
 */

// @lc code=start
function longestPalindrome(s: string): string {
  let res = '';
  for (let i = 0; i < s.length; i++) {
    let p1 = getPalindrome(i, i);
    let p2 = getPalindrome(i, i + 1);

    res = p1.length > res.length ? p1 : res;
    res = p2.length > res.length ? p2 : res;
  }

  return res;

  function getPalindrome(i, j) {
    while (i >= 0 && j < s.length) {
      if (s[i] !== s[j]) break;

      i--;
      j++;
    }

    return s.substring(i + 1, j);
  }
}

// @lc code=end
