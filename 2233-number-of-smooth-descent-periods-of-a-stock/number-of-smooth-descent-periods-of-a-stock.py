class Solution:
    def getDescentPeriods(self, prices: list[int]) -> int:
        start,end = 0,0
        count = len(prices)
        while end < len(prices):
            if prices[start] - prices[end] == end-start:
                end += 1
            else:
                n = end - start - 1
                count += int(n*(n+1)/2)
                start = end

        n = end - start - 1
        count += int(n*(n+1)/2)
        return count


        