/*
 * @lc app=leetcode.cn id=239 lang=java
 * @lcpr version=30204
 *
 * [239] 滑动窗口最大值
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;

class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        var q = new ArrayDeque<Integer>();
        var res = new ArrayList<Integer>();

        for (int r = 0; r < nums.length; r++) {

            while (!q.isEmpty() && nums[r] > nums[q.getLast()]) {
                q.removeLast();
            }
            q.addLast(r);

            if (r < k - 1) {
                continue;
            }

            res.add(nums[q.getFirst()]);

            int l = r - k + 1;
            int removed = nums[l];
            if (nums[q.getFirst()] == removed) {
                q.removeFirst();
            }
        }

        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}
// @lc code=end

/*
 * // @lcpr case=start
 * // [-7,-8,7,5,7,1,6,0]\n4\n
 * // @lcpr case=end
 * 
 * // @lcpr case=start
 * // [1]\n1\n
 * // @lcpr case=end
 * 
 */
