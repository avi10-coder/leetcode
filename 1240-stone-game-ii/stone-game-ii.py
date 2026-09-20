class Solution:

    def dfs(self, dp, piles, index, M):
        # index -> Alice starting index
        max_result = 0
        for X in range(1,2*M+1):
            #X -> number of piles alice picked
            if index + X > len(piles):
                break
            M_new = max(M,X)

            if dp[index + X][M_new] is None:
                dp[index + X][M_new] = self.dfs(dp, piles, index + X, M_new)
                
            competetor = dp[index + X][M_new]
            collected = sum(piles[index:index+X])
            remaining = sum(piles[index+X:]) - competetor
            result = collected + remaining
            max_result = max(max_result,result)

        return max_result

    def stoneGameII(self, piles: list[int]) -> int:
        dp = [[None for i in range(2*len(piles))] for j in range(len(2*piles))]
        return self.dfs(dp, piles, 0, 1)
        