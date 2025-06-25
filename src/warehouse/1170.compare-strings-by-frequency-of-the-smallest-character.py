#
# @lc app=leetcode.cn id=1170 lang=python3
# @lcpr version=30204
#
# [1170] 比较字符串最小字母出现频次
#


# @lcpr-template-start
from bisect import bisect_right
from typing import List, Optional
from lct import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str):
            arr  =s.split('')
            arr.sort()
            i = bisect_right(arr, arr[0])
            return i
        
        words = [f(w) for w in words]
        words.sort()
        queries = [f(q) for q in queries]

        res = []
        for q in queries:
            i = bisect_right(words, q)
            res.append(len(words) - i)
        
        return res
# @lc code=end



#
# @lcpr case=start
# ["cbd"]\n["zaaaz"]\n
# @lcpr case=end

# @lcpr case=start
# ["bbb","cc"]\n["a","aa","aaa","aaaa"]\n
# @lcpr case=end

#

