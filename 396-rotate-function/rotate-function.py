class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        arr_sum = sum(nums) # O(n)
        n = len(nums) # O(n)
        total = 0
        mx = 0
        for i in range(n): # O(n)
            total +=  arr_sum - n*nums[n-i-1]
            mx = max(mx,total)
        return sum([i*nums[i] for i in range(n)]) + mx # O(n)





        