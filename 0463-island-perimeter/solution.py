class Solution:
    def islandPerimeter(self, g: List[List[int]]) -> int:
        return abs(__import__('scipy').signal.convolve2d(g,[[-2,1],[1,0]])).sum()
