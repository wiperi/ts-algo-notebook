/*
 * @lc app=leetcode.cn id=76 lang=java
 * @lcpr version=30204
 *
 * [76] 最小覆盖子串
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

import java.util.HashMap;

class Solution {
    public String minWindow(String s, String t) {
        var tarMp = new HashMap<Character, Integer>();
        for (var c : t.toCharArray()) {
            tarMp.put(c, tarMp.getOrDefault(c, 0));
        }

        var mp = new HashMap<Character, Integer>();
        var ss = s.toCharArray();
        int l = 0;
        int r = 0;
        String res = String.valueOf(ss);
        while (r < s.length()) {
            char c = ss[r];
            if (tarMp.containsKey(c)) {
                mp.put(c, mp.getOrDefault(c, 0));
            }
            r += 1;

            boolean found = false;
            while (l < r && mp.equals(tarMp)) {
                found = true;
                char rm = ss[l];
                if (tarMp.containsKey(rm)) {
                    mp.put(rm, mp.get(rm) - 1);
                }
            }
            if (found) {
                String localRes = s.substring(l - 1, r);
                if (localRes.length() < res.length()) {
                    res = localRes;
                }
            }
        }

        return res;
    }
}
// @lc code=end

/*
 * // @lcpr case=start
 * // "ADOBECODEBANC"\n"ABC"\n
 * // @lcpr case=end
 * 
 * // @lcpr case=start
 * // "a"\n"a"\n
 * // @lcpr case=end
 * 
 * // @lcpr case=start
 * // "a"\n"aa"\n
 * // @lcpr case=end
 * 
 */
