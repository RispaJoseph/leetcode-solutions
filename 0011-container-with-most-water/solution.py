class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(height) - 1

        while l < r:
            if height[l] > height[r]:
                area = height[r] * (r-l)
                r -= 1
            else:
                area = height[l] * (r-l)
                l += 1
            maxarea = max(maxarea, area)
        return maxarea  
        
