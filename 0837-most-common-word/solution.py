class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.replace("!"," ").replace("?", " ").replace("'"," ").replace(","," ").replace(";"," ").replace("."," ")

        ans, dict1, banned = paragraph.split(), defaultdict(int), set(banned)

        for i in ans:
            if i.lower() not in banned:
                dict1[i.lower()] += 1

        max_val = max(dict1.values())

        return [key for key,val in dict1.items() if val == max_val][0]
