# 这个方法绝对会超时的...想都能想得到
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 10 ** n - 1
        ansnum = 0
        while num >= 10 ** (n - 1):
            num2 = 10 ** n - 1
            while num2 >= 10 ** (n - 1):
                ans = num * num2
                ans = str(ans) 
                if ans == ans[::-1] and int(ans) > ansnum:
                    ansnum = int(ans)
                num2 -=1
            num -= 1
        return ansnum%1337

    list = range(5, 2, -1)
    for i in list:
        print(i)

    #好了一点，依旧超时
    class Solution(object):
        def largestPalindrome(self, n):
            """
            :type n: int
            :rtype: int
            """
            if n == 1:
                return 9
            num_high = 10 ** n - 1
            num_low = 10 ** (n - 1)
            for i in range(num_high, num_low - 1, -1):
                ans = str(i) + str(i)[::-1]
                ans = int(ans)
                for j in range(num_high, num_low - 1, -1):
                    if ans // j > num_high:
                        break
                    if ans % j == 0:
                        return ans % 1337

    #算法真他妈有趣啊
    class Solution(object):
        def largestPalindrome(self, n):
            """
            :type n: int
            :rtype: int
            """
            # https://discuss.leetcode.com/topic/98590/python-solution-using-math-in-48ms
            """
            I used the following approach. Let's denote the biggest palindrome product as palindrome = M * L. For N > 1
            this palidrome has even number of digits and it can be represented as the sum:
            palindrome = upper * 10^N + lower
            We can expect that M and L are close to 10^N and we can represent them as M = 10^N - i, L = 10^N - j and hence
            palindrome = (10^N - i) * (10^N - j) = 10^N * (10^N - (i + j)) + i * j
            If we assume that i * j < 10^N (this assumption turned out to be true for N > 1) we can represent upper and lower in the following way:
            upper = 10^N - (i + j)
            lower = i * j
            This is the system of equations which can be solved if we know upper and lower. Let's denote sum of i and j as a = i + j.
            It can be calculated as a = 10^N - upper. Because j = a - i equation for lower can be rewritten as:
            lower = a * i - i * i
            This is a quadratic equation which can be solved using standard methods from textbooks.
            Thanks to @nizametdinov 's reply in this thread, I came out below solution.
            Because i^2 - a*i - lower = 0
            thus, (i-a/2)^2 = (4*lower-a^2)/2
            thus, i.f.f. (4*lower-a^2)/2 is some integer's square, can lower i^2 - a*i - lower = 0 have integer result.
            so I use (a^2-4*lo)^.5 == int((a^2-4*lo)^.5) to check.
            """

            if n == 1: return 9
            if n == 2: return 987
            for a in range(2, 9 * 10 ** (n - 1)):
                hi = (10 ** n) - a
                lo = int(str(hi)[::-1])
                if a ** 2 - 4 * lo < 0: continue
                if (a ** 2 - 4 * lo) ** .5 == int((a ** 2 - 4 * lo) ** .5):
                    return (lo + 10 ** n * (10 ** n - a)) % 1337