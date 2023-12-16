class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a = list(zip(names, heights))
        s = sorted(a, key=lambda x:x[1], reverse=True)

        sorting = [x for x,y in s]
        return sorting
        
