class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set: set = set(nums)
        res: int = 0
        for i in num_set:
            if (i-1) not in num_set:
                num = i
                streak = 1
                while (num+1) in num_set:
                    num += 1
                    streak += 1
                res = max(res, streak)
        return res