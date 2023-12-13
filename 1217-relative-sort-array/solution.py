class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        for i in arr2:
            s = arr1.count(i)
            for j in range(s):
                arr3.append(i)
        arr1.sort()
        for k in arr1:
            if k not in arr2:
                arr3.append(k)
        return arr3
