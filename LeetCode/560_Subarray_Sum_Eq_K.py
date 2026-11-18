class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count: int = 0
        pref: int = 0
        pref_cnt: dict = {0: 1}
        for i in nums:
            pref += i
            if (pref - k) in pref_cnt:
                count += pref_cnt[pref - k]
            if pref in pref_cnt:
                pref_cnt[pref] += 1
            else:
                pref_cnt[pref] = 1
        return count