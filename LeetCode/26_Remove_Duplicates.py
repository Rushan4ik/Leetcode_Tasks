class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen: set = set()
        k: int = 0
        for i in nums:
            if i not in seen:
                seen.add(i)
                nums[k] = i
                k += 1
        return k