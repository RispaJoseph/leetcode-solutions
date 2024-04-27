class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in parentheses.values():
                stack.append(char)
            elif char in parentheses.keys():
                if not stack or stack.pop() != parentheses[char]:
                    return False
        return not stack

