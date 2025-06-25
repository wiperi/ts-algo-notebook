#
# @lc app=leetcode.cn id=911 lang=python3
# @lcpr version=30204
#
# [911] 在线选举
#


# @lcpr-template-start
import bisect
from collections import defaultdict
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        n = len(persons)

        leading = [0] * n

        freq = defaultdict(int)
        leader = persons[0]

        for i, person in enumerate(persons):
            freq[person] += 1
            if freq[person] >= freq[leader]:
                leader = person
            leading[i] = leader
        
        self.leading = leading
        self.times = times

    def q(self, t: int) -> int:

        index = bisect.bisect_left(self.times, t)
        if index >= len(self.times) or self.times[index] != t:
            index -= 1

        return self.leading[index]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end



#
# @lcpr case=start
# ["TopVotedCandidate", "q", "q", "q", "q", "q", "q"][[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]\n
# @lcpr case=end

#

