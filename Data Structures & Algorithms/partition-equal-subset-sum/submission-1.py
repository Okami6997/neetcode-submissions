class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            ndp = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                ndp.add(t + nums[i])
                ndp.add(t)
            dp = ndp
        return False