#
# @lc app=leetcode.cn id=739 lang=python3
# @lcpr version=30204
#
# [739] 每日温度
#


# @lcpr-template-start
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode


# @lcpr-template-end
# @lc code=start
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st = []
        n = len(temp)

        res = [0] * n
        # find next large
        for i in reversed(range(n)):
            while st and temp[i] >= temp[st[-1]]:
                st.pop()

            res[i] = st[-1] - i if st else 0
            st.append(i)

        return res



# @lc code=end


#
# @lcpr case=start
# [73,74,75,71,69,72,76,73]\n
# @lcpr case=end

# @lcpr case=start
# [30,40,50,60]\n
# @lcpr case=end

# @lcpr case=start
# [30,60,90]\n
# @lcpr case=end

#
