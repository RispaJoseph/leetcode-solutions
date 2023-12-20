class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        _set: set[str] = set(words[0])
        answer: list[str] = []

        for word in words:
            _set &= set(word)

        for word in _set:
            answer.extend([word] * min([_word.count(word) for _word in words]))

        return answer
        
