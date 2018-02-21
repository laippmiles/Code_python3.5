#76ms
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for i in range(1,n+1):
            if i % 15 == 0:
                ans.append('FizzBuzz')
                continue
            if i % 3 == 0:
                ans.append('Fizz')
                continue
            if i % 5 == 0:
                ans.append('Buzz')
                continue
            ans.append(str(i))
        return ans