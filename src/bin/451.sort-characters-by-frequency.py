#
# @lc app=leetcode.cn id=451 lang=python3
# @lcpr version=30204
#
# [451] 根据字符出现频率排序
#


# @lcpr-template-start
from collections import Counter
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        # print(c)

        # print(c.items())
        # print(list(c.items()))
        arr = sorted(list(c.items()), key=lambda a:a[1], reverse=True)

        # print(arr)

        res = []
        for pair in arr:
            ch = pair[0]
            freq = pair[1]

            for i in range(freq):
                res.append(ch)

        # print(res)

        return ''.join(res)
# @lc code=end



#
# @lcpr case=start
# "tree"\n
# @lcpr case=end

# @lcpr case=start
# "cccaaa"\n
# @lcpr case=end

# @lcpr case=start
# "Aabb"\n
# @lcpr case=end

#

