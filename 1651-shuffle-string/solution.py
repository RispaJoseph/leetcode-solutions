class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        shuffle = ""
        for i in range(len(indices)):
            shuffle += (s[indices.index(i)])
        return shuffle
