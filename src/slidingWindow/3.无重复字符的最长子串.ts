/*
 * @lc app=leetcode.cn id=3 lang=typescript
 *
 * [3] 无重复字符的最长子串
 */

// @lc code=start
function lengthOfLongestSubstring(s: string): number {
  // 只有当s[right]不会导致重复的时候加入窗口
  // 每次合法更新窗口后，更新res

  if (s.length <= 1) return s.length;

  let [left, right] = [0, 0];

  let window = new Set();
  let res = 0;

  while (right < s.length) {

    // 检查即将更新的窗口是否合法
    while (window.has(s[right])) {
      window.delete(s[left]);
      left++;
    }

    // 更新窗口
    window.add(s[right]);

    res = Math.max(res, window.size);

    right++;
  }

  return res;
}
// @lc code=end

if (require.main === module) {
  let res = lengthOfLongestSubstring('dvdf');
  console.log(res);
}

export {};
