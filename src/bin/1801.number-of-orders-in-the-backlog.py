#
# @lc app=leetcode.cn id=1801 lang=python3
# @lcpr version=30204
#
# [1801] 积压订单中的订单总数
#


# @lcpr-template-start
from heapq import heappop, heappush
from typing import List, Optional
from src.adt.py.leetcodeType import ListNode, TreeNode
# @lcpr-template-end
# @lc code=start
def hpush(pq, val):
    newval = [v for v in val]
    newval[0] *= -1
    heappush(pq, newval)

def hpop(pq):
    return heappop(pq)

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # sell
        minpq = []
        # buy
        maxpq = []

        for order in orders:
            if order[2] == 0:
                # buy
                buyPrice = order[0]
                buyAmount = order[1]

                # try to buy
                while minpq:
                    sellOrder = heappop(minpq)
                    sellPrice = sellOrder[0]
                    sellAmount = sellOrder[1]

                    if not (buyPrice >= sellPrice): 
                        heappush(minpq, (sellPrice, sellAmount))
                        break

                    dealAmount = min(buyAmount, sellAmount)
                    # print('deal buy', dealAmount, buyPrice, sellPrice)
                    sellAmount -= dealAmount
                    buyAmount -= dealAmount

                    if sellAmount != 0:
                        heappush(minpq, (sellPrice, sellAmount))
                    if buyAmount == 0: break

                if buyAmount > 0:
                    hpush(maxpq, (buyPrice, buyAmount))

            elif order[2] == 1:
                # sell
                sellPrice = order[0]
                sellAmount = order[1]

                # try to sell
                while maxpq:
                    buyOrder = heappop(maxpq)
                    buyPrice = -buyOrder[0]
                    buyAmount = buyOrder[1]

                    if not (buyPrice >= sellPrice): 
                        hpush(maxpq, (buyPrice, buyAmount))
                        break

                    dealAmount = min(buyAmount, sellAmount)
                    # print('deal sell', dealAmount, buyPrice, sellPrice)
                    buyAmount -= dealAmount
                    sellAmount -= dealAmount

                    if buyAmount != 0:
                        hpush(maxpq, (buyPrice, buyAmount))
                    if sellAmount == 0: break

                if sellAmount > 0:
                    heappush(minpq, (sellPrice, sellAmount))

        # print(minpq)
        # print(maxpq)
        MOD = 10**9 + 7
        amountLeft = 0
        for order in minpq:
            amountLeft += (order[1] % MOD)
        
        for order in maxpq:
            amountLeft += (order[1] % MOD)

        return amountLeft % MOD
        
# @lc code=end



#
# @lcpr case=start
# [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]\n
# @lcpr case=end

#

