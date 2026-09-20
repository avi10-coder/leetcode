class Solution:

    def dfs(self, dp, piles, start, end):
        """
        return max of stones player can win from given state
        """
        if start == end:
            return piles[start]
        
        # pick from left
        player = piles[start]
        if dp[start+1][end] == -1:
            dp[start+1][end] = self.dfs(dp, piles, start+1,end)
        competetor = dp[start+1][end]
        remaining = sum(piles[start+1:end+1])
        result_left = player + (remaining-competetor)

        # pick from right
        player = piles[end]
        if dp[start][end-1] == -1:
            dp[start][end-1] = self.dfs(dp, piles, start,end-1)
        competetor = dp[start][end-1]
        remaining = sum(piles[start:end])
        result_right = player + (remaining-competetor)

        return max(result_left,result_right)


    def stoneGame(self, piles: list[int]) -> bool:
        dp = [[-1 for i in range(len(piles))] for j in range(len(piles))]
        alice = self.dfs(dp, piles, 0, len(piles)-1)
        bob = sum(piles) - alice
        if alice > bob:
            return True
        else:
            return False
        