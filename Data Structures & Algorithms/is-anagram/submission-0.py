from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = Counter(s)
        y = Counter(t)
        l = sorted(x.items())
        l1 = sorted(y.items())
        return l == l1