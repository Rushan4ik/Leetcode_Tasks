from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        data: dict = defaultdict(list)
        for i in strs:
            data[tuple(sorted(i))].append(i)
        return list(data.values())