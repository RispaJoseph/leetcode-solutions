class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count={}
        for i in s:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        unique_counts = set(count.values())
        return len(unique_counts) == 1

                
