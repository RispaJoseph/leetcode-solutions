class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        string = str(nums)
        new = []
        for i in string:
            if i.isnumeric():
                new.append(int(i))
        return(new)
