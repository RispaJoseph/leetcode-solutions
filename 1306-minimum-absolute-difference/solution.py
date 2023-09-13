class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        new, min = [], arr[1] - arr[0]
        for i in range(len(arr)-1):
            if min > arr[i+1] - arr[i]:
                min = arr[i+1] - arr[i]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == min: 
                new.append([arr[i], arr[i+1]])
        return new
