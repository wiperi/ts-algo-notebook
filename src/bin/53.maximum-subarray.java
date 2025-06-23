/*
 * @lc app=leetcode.cn id=53 lang=java
 * @lcpr version=30204
 *
 * [53] 最大子数组和
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start
class Solution {
    public int maxSubArray(int[] nums) {
        // f(x) = max(f(x - 1), 0) + nums[x]
        int f0 = nums[0];
        int res = nums[0];

        for (int i = 1; i < nums.length; i++) {
            f0 = Math.max(f0, 0) + nums[i];
            res = Math.max(res, f0);
        }

        return res;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [-2,1,-3,4,-1,2,1,-5,4]\n
// @lcpr case=end

// @lcpr case=start
// [1]\n
// @lcpr case=end

// @lcpr case=start
// [5,4,-1,7,8]\n
// @lcpr case=end

 */

