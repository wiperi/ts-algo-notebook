/*
 * @lc app=leetcode.cn id=215 lang=java
 * @lcpr version=30204
 *
 * [215] 数组中的第K个最大元素
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

import java.util.Comparator;
import java.util.PriorityQueue;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minPQ = new PriorityQueue<>();

        for (int n : nums) {
            minPQ.add(n);
            if (minPQ.size() > k) {
                minPQ.poll();
            }
        }

        return minPQ.poll();
    }
}
// @lc code=end



/*
// @lcpr case=start
// 2\n
// @lcpr case=end

// @lcpr case=start
// 4\n
// @lcpr case=end

 */

