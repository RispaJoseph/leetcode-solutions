class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        unique = []
        for i in nums:
            if nums.count(i) == 1:
                unique.append(i)
        return sum(unique) 
        

