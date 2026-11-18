class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        r: int = 0
        l: int = len(nums) - 1
        while r <= l:
            if nums[r] == val:
                nums[r] = nums[l]
                l -= 1
            else:
                r += 1
        return l + 1
        