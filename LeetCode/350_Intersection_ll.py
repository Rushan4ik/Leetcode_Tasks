from collections import Counter
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        cnt1, cnt2 = Counter(nums1), Counter(nums2)
        data: dict = {}
        for i in (cnt1+cnt2).keys():
            data[i] = min(cnt1[i], cnt2[i])

        return [key for key, value in data.items() for _ in range(value)]


