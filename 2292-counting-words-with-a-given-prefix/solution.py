class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        count = 0
        l = len(pref)
        list = []
        print(l)

        for i in words:
            x = i[:l]
            list.append(x)
        for j in list:
            if j == pref:
                count+=1
        return count
        
