class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(s)
        a = ""
        for i in l:
            if i == '?' or i == ' ' or i == ',' or i == "'" or i == '.' or i ==':' or i == ';':
                continue
            else:
                a += i
        a = a.lower()
        if a == a[::-1]:
            return True
        else:
            return False
