class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        new = []
        for i in range(len(words)):
            a = words[i]
            if x in list(a):
                new.append(i)
        return new
        
