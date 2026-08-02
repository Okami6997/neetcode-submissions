class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # numSet = set(nums)
        # return len(nums) != len(numSet)
        ns = set()
        for i in nums:
            if i in ns:
                return False
        return True
