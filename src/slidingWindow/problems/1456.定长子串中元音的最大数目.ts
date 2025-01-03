/*
 * @lc app=leetcode.cn id=1456 lang=typescript
 *
 * [1456] 定长子串中元音的最大数目
 */

// @lc code=start
function maxVowels(s: string, k: number): number {
  // 维护一个定长窗口，向右移动，每次计算并挑战原元音字母数量

  let vowel = new Set('aeiou')
  let win = 0;
  let res = 0;

  let left = 0, right = k - 1;

  for (let i = left; i <= right; i++) {
    if (vowel.has(s[i])) {
      win++;
    }
  }
  res = win;


  right = k;
  while (right < s.length) {
    // remove left
    if (vowel.has(s[left])) win--;
    // add right
    if (vowel.has(s[right])) win++;

    res = Math.max(res, win);

    right++;
    left++;
  }

  return res;
}
// @lc code=end
