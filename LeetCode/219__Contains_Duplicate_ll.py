class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen: dict = {}
        for i, num in enumerate(nums, start = 0):
            if num in seen:
                if abs(seen[num] - i) <= k:
                    return True
            seen[num] = i
        return False