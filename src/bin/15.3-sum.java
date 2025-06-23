/*
 * @lc app=leetcode.cn id=15 lang=java
 * @lcpr version=30204
 *
 * [15] 三数之和
 */

// @lcpr-template-start

// @lcpr-template-end
// @lc code=start

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        var res = new ArrayList<List<Integer>>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int j = i + 1;
            int k = nums.length - 1;
            int target = -nums[i];

            int smallestSum = nums[i] + nums[j] + nums[j + 1];
            int largestSum = nums[i] + nums[k] + nums[k - 1];
            if (smallestSum > 0) {
                break;
            }
            if (largestSum < 0) {
                continue;
            }

            while (j < k) {
                int sum = nums[j] + nums[k];

                if (sum == target) {
                    res.add(List.of(nums[i], nums[j], nums[k]));
                    k -= 1;
                    while (j < k && nums[k] == nums[k + 1]) {
                        k -= 1;
                    }
                    j += 1;
                    while (j < k && nums[j] == nums[j - 1]) {
                        j += 1;
                    }
                } else if (sum > target) {
                    k -= 1;
                } else {
                    j += 1;
                }
            }
        }

        return res;

    }
}
// @lc code=end

/*
 * // @lcpr case=start
 * // [-1,0,1,2,-1,-4]\n
 * // @lcpr case=end
 * 
 * // @lcpr case=start
 * // [0,1,1]\n
 * // @lcpr case=end
 * 
 * // @lcpr case=start
 * // [0,0,0]\n
 * // @lcpr case=end
 * 
 */
