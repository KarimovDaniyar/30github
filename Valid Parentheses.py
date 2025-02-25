class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {'[':']', '{':'}', '(':')'}
        for i in s:
            if i in pairs:
                stack.append(i)
            else:
                if not stack or pairs[stack.pop()] != i:
                    return False
        return not stack
                
                
s = Solution()
print(s.isValid("({[})"))