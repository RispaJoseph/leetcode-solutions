class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        new = []
        for i in range(1, n+1):
            if i not in num_set:
                new.append(i)
        return new
        
