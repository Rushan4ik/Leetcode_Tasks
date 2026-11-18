class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return list(set(i for i in range(1, len(nums)+1)) - set(nums))[0]


