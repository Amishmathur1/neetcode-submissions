class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        tb = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if stack and stack[-1] == tb[i]:
                    stack.pop()
                else:
                    return False
        if len(stack) != 0:
            return False
        return True