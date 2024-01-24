class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        l = []
        for i in words:
            if i and i[::-1] in l:
                count += 1
            else:
                l.append(i)
        return count

        
