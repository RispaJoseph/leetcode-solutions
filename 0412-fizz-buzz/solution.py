class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        i = 0
        result = []
        while i <= n-1:
            i +=1
            if i%3 == 0 and i%5 == 0:
                result.append("FizzBuzz")
            elif i%5 == 0:
                result.append("Buzz")
            elif i%3 == 0:
                result.append("Fizz")
            else:
                result.append(str(i))
        return result

        
