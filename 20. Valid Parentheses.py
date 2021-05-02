class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ')':
                if stack == []:
                    return False
                if stack.pop()!= '(':
                    print(stack)
                    return False
            elif i == '}':
                if stack == []:
                    return False
                if stack.pop()!= '{':
                    return False
            elif i == ']':
                if stack == []:
                    return False
                if stack.pop()!= '[':
                    return False
            else:
                stack.append(i)
        if stack == []:
            return True
        return False
                