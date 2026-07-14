class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s += str(i)        
        s = str(int(s) + 1)
        l = [int(i) for i in s]
        return l
    