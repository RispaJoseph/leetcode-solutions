class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        s = []
        for i in range(1,len(nums)+1):
            if n%i == 0:
                s.append(nums[i-1])
        sq = [i**2 for i in s]
        return (sum(sq))
        
