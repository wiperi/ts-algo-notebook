/*
 * @lc app=leetcode.cn id=76 lang=typescript
 *
 * [76] 最小覆盖子串
 */

// @lc code=start
function minWindow(s: string, t: string): string {

  // 伪代码：
  // while (right < s.length) {

  //   s[right] add to window;

  //   while (window cover t) {
  //     res update;
  //     shrink window;
  //     left++;

  //   }
  //   right++;
  // }

  let left = 0;
  let right = 0;

  let window = '';
  let res = '';

  while (right <= s.length) {
    window = s.substring(left, right);

    while (cover(window, t)) {
      if (window.length < res.length || res.length === 0) {
        res = window;
      }
      left++;
      window = s.substring(left, right);
    }

    right++;
  }

  return res;

  function cover(s: string, t: string) {
    let src = s.split('');
    let tar = t.split('');

    return tar.every(c => {
      let i = src.indexOf(c);
      if (i === -1) return false;

      src.splice(i, 1);
      return true;
    });
  }
}
// @lc code=end
if (require.main === module) {
  console.log(minWindow('aba', 'b'));
}
