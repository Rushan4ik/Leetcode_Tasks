from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, j in enumerate(s, start = 0):
            if cnt[j] == 1:
                return i
        return -1