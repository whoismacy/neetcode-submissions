# what could be the possible outcomes?
# where should l and r start?
"""
l is bigger than r
    move l forward
l is lesser than r
    calculate the difference update
they are both equal
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        l = 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                maxx = max(maxx, prices[r] - prices[l])

        return max(maxx, 0)
        