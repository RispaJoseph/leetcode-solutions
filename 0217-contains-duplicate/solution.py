class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)
        l1 = len(new)
        l2 = len(nums)

        if l1 == l2:
            return False
        else:
            return True
        
