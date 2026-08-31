class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # visited = []
        # for i in range(len(nums)):
        #     if target - nums[i] in visited:
        #         return [nums.index(target - nums[i]), i]
        #     else:
        #         visited.append(nums[i])
        prevMap = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i