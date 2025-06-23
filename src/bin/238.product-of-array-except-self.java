/*
 * @lc app=leetcode.cn id=238 lang=java
 * @lcpr version=30204
 *
 * [238] 除自身以外数组的乘积
 */


// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

import java.util.Arrays;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = nums.clone();
        Arrays.fill(res, 1);

        int p = 1;
        for (int i = 0;i < nums.length; i++) {
            res[i] *= p;
            p *= nums[i];
        }
        p = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            res[i] *= p;
            p *= nums[i];
        }

        return res;
    }
}
// @lc code=end



/*
// @lcpr case=start
// [1,2,3,4]\n
// @lcpr case=end

// @lcpr case=start
// [-1,1,0,-3,3]\n
// @lcpr case=end

 */

