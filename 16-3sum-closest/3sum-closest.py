class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        diff = -10**5
        closest = -10**5
        exact = 0
        for i in range(len(nums)-1):
            if exact:
                return target
            start,end = i+1,len(nums)-1
            while start < end:
                sm = nums[i] + nums[start] + nums[end]
                current_diff = abs(target - sm)
                if abs(current_diff) < abs(diff):
                    closest = sm
                    diff = current_diff
                else:
                    pass
                if sm < target:
                    start += 1
                elif sm > target:
                    end -= 1
                else:
                    exact = 1
                    break
        return closest

                    