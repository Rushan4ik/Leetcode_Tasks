class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res: int = 0
        for i in nums:
            res ^= i
        return res

