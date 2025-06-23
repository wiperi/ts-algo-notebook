/*
 * @lc app=leetcode.cn id=560 lang=java
 * @lcpr version=30204
 *
 * [560] 和为 K 的子数组
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

import java.util.HashMap;

class Solution {
    public int subarraySum(int[] nums, int k) {
        var pre = new int[nums.length + 1];
        for (int i = 1; i < nums.length + 1; i++) {
            pre[i] = pre[i - 1] + nums[i - 1];
        }

        // pre[j] - pre[i] = K
        // pre[i] = pre[j] - k
        int cnt = 0;
        var mp = new HashMap<Integer, Integer>();
        mp.put(0, 1);
        for (int j = 1; j < pre.length; j++) {
            if (mp.containsKey(pre[j] - k)) {
                cnt += mp.get(pre[j] - k);
            }

            mp.put(pre[j], mp.getOrDefault(pre[j], 0) + 1);
        }

        return cnt;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [1,1,1]\n2\n
// @lcpr case=end

// @lcpr case=start
// [1,2,3]\n3\n
// @lcpr case=end

 */

