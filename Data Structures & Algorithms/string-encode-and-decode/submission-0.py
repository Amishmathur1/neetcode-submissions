from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # 1. Find the position of '#'
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # length of the next string
            # 2. Extract the string of given length
            word = s[j+1:j+1+length]
            res.append(word)
            # 3. Move pointer to next encoded string
            i = j + 1 + length
        return res
