class Solution:

    def dfs(self, nums, index, target, dp):

        if index == len(nums):
            return 1 if target == 0 else 0

        if (index, target) in dp:
            return dp[(index, target)]

        # Put '+' before nums[index]
        count1 = self.dfs(
            nums,
            index + 1,
            target - nums[index],
            dp
        )

        # Put '-' before nums[index]
        count2 = self.dfs(
            nums,
            index + 1,
            target + nums[index],
            dp
        )

        dp[(index, target)] = count1 + count2

        return dp[(index, target)]

    def findTargetSumWays(self, nums, target):
        dp = {}
        return self.dfs(nums, 0, target, dp)