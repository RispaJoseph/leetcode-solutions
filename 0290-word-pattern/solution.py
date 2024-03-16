class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split()
        list1 = []
        list2 = []

        for i in pattern:
            list1.append(pattern.index(i))
        
        for i in l:
            list2.append(l.index(i))

        if list1 == list2:
            return True
        else:
            return False
