class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            mh = target - nums[i]
            if mh in seen:
                return [seen[mh], i]
            else:
                seen[nums[i]] = i