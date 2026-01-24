class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        current = 0

        for i in range(k):
            if s[i] in vowels:
                current += 1

        max_vowels = current
        for i in range(k, len(s)):
            if s[i] in vowels:
                current += 1
            if s[i-k] in vowels:
                current -= 1
            max_vowels = max(max_vowels, current)
        return max_vowels
        
