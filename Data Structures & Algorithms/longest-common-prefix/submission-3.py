class Solution:
    def longestCommonPrefix(self, strs: List[str]):

        ind = 0
        res = ""

        while ind < len(strs[0]):

            for word in strs:
                if ind >= len(word) or word[ind] != strs[0][ind]:
                    return res

            res += strs[0][ind]
            ind += 1

        return res