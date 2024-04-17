class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        new = Counter(nums)
        a = [key for key,value in new.items() if value == 1]
        return a

        
