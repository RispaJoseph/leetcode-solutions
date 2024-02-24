class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while len(nums) > 0:
            A = min(nums)
            nums.remove(A)
            B = min(nums)
            nums.remove(B)
            arr.append(B)
            arr.append(A)
        return arr
        
