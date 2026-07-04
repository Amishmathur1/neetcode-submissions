class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        ans = ''
        for i in range(min(len(word1), len(word2))):
            ans += word1[l] + word2[l]
            l += 1
        
        x = len(word1)
        y = len(word2)
        if x > y:
            ans += word1[l:x]
        else:
            ans += word2[l:y]
        return ans