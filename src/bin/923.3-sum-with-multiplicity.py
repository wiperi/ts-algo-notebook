#
# @lc app=leetcode.cn id=923 lang=python3
# @lcpr version=30204
#
# [923] 三数之和的多种可能
#


# @lcpr-template-start
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def threeSumMulti(self, a: List[int], target: int) -> int:
        mp = Counter(a)
        a.sort()
        n = len(a)
        cnt = 0
        
        for i in range(n - 2):
            t = target - a[i]

            j, k = i + 1, n - 1
            while j < k:
                s = a[j] + a[k]

                if s == t and a[j] == a[k]:
                    length = k - j + 1
                    cnt += length * (length - 1) // 2
                    break
                elif s == t:
                    left_len = right_len = 1
                    j += 1
                    while j < k and a[j] == a[j - 1]:
                        left_len += 1
                        j += 1
                    k -= 1
                    while j < k and a[k] == a[k + 1]:
                        right_len += 1
                        k -= 1
                    cnt += left_len * right_len
                elif s < t:
                    j += 1
                else:
                    k -= 1
                
            # print(cnt, i, a[i])

        return cnt
# @lc code=end



#
# @lcpr case=start
# [1,1,2,2,3,3,4,4,5,5]\n8\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,2,2,2]\n5\n
# @lcpr case=end

#

