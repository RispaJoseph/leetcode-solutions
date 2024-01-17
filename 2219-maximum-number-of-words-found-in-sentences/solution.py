class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum = []
        for i in range(len(sentences)):
            a = sentences[i].split(' ')
            maximum.append(len(a))
        return max(maximum)
