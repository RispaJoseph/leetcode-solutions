class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        stack = []
        result = []

        for i in s:
            if i in vowels:
                stack.append(i)
        for i in s:
            if i in vowels:
                result.append(stack.pop())
            else:
                result.append(i)
        return ''.join(result)

        
