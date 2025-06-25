/*
 * @lc app=leetcode.cn id=3 lang=java
 * @lcpr version=30204
 *
 * [3] 无重复字符的最长子串
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        var arr = s.toCharArray();

        var cnt = new int[128];

        int l = 0;
        int r = 0;
        int res = 0;

        while (r < arr.length) {
            char c = arr[r];
            cnt[c] += 1;
            r += 1;

            while (l < r && cnt[c] > 1) {
                cnt[arr[l]] -= 1;
                l += 1;
            }

            res = Math.max(res, r - l);

        }

        return res;
    }
}
// @lc code=end

/*
 * // @lcpr case=start
 * // "abcabcbb!@#"\n
 * // @lcpr case=end
 * 
 * // @lcpr case=start
 * // "bbbbb"\n
 * // @lcpr case=end
 * 
 * // @lcpr case=start
 * // "pwwkew"\n
 * // @lcpr case=end
 * 
 */
