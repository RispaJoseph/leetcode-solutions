class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s = Counter(s)
        target = Counter(target)
        return min(s[i] // target[i] for i in target)

        
