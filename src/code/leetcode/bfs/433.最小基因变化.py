#
# @lc app=leetcode.cn id=433 lang=python3
# @lcpr version=30104
#
# [433] 最小基因变化
#
from typing import List, Optional

from adt.py.leetcodeType import ListNode
# @lc code=start
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        res = 0

        n = len(startGene)
        q = [startGene]
        bank_set: set = set(bank)
        visited = set()

        while q:
            size = len(q)
            for _ in range(size):
                curr = q.pop(0)

                if curr == endGene:
                    return res

                for i in range(n):
                    for c in ["A", "C", "T", "G"]:
                        if c == curr[i]:
                            continue

                        mutation = curr[:i] + c + curr[i + 1 :]

                        if mutation not in bank_set or mutation in visited:
                            continue

                        visited.add(mutation)
                        q.append(mutation)
            res += 1

        return -1


# @lc code=end


#
# @lcpr case=start
# "AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]\n
# @lcpr case=end

# @lcpr case=start
# "AACCGGTT"\n"AAACGGTA"\n["AACCGGTA","AACCGCTA","AAACGGTA"]\n
# @lcpr case=end

# @lcpr case=start
# "AAAAACCC"\n"AACCCCCC"\n["AAAACCCC","AAACCCCC","AACCCCCC"]\n
# @lcpr case=end

#
