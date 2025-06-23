/*
 * @lc app=leetcode.cn id=438 lang=java
 * @lcpr version=30204
 *
 * [438] 找到字符串中所有字母异位词
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        if (p.length() > s.length()) {
            return new ArrayList<>();
        }

        var win = new int[26];
        var ss = s.toCharArray();
        var pp = p.toCharArray();

        for (int i = 0; i < p.length(); i++) {
            win[ss[i] - 'a'] += 1;
            win[pp[i] - 'a'] -= 1;
        }

        var pq = new PriorityQueue<Integer>((a, b) -> a - b);

        int diff = 0;
        for (var n : win) {
            if (n != 0) {
                diff += 1;
            }
        }

        var res = new ArrayList<Integer>();
        if (diff == 0) {
            res.add(0);
        }

        int l = 0;
        int r = p.length();

        while (r < s.length()) {
            char added = ss[r];
            if (win[added - 'a'] == -1) {
                diff -= 1;
            }
            else if (win[added - 'a'] == 0) {
                diff += 1;
            }
            win[added - 'a'] += 1;
            r += 1;

            char removed = ss[l];
            if (win[removed - 'a'] == 1) {
                diff -= 1;
            }
            else if (win[removed - 'a'] == 0) {
                diff += 1;
            }
            win[removed - 'a'] -= 1;
            l += 1;

            if (diff == 0) {
                res.add(l);
            }
        }

        return res;
    }
}
// @lc code=end



/*
// @lcpr case=start
// "cbaebabacd"\n"abc"\n
// @lcpr case=end

// @lcpr case=start
// "abab"\n"ab"\n
// @lcpr case=end

 */

