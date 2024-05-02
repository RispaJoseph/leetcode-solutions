class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr = list(map(lambda n:n**2,nums))
        sqr.sort()
        return sqr
        
