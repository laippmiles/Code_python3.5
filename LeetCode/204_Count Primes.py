#access不了的超时法
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n >= 0 and n <= 2:
            return 0
        elif n == 3:
            return 1
        elif n == 4:
            return 2
        else:
            import math

            ans = 2
            for i in range(5, n):
                Flag = 0
                for j in range(2, i):
                    if i % j == 0:
                        Flag = 1
                        break
                if Flag == 0:
                    ans += 1
            return ans

print(int(3**0.5))

#别人家的132ms
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        import numpy as np
        primes = np.ones(n / 2, dtype=np.bool)
        for i in range(3, int(n ** 0.5) + 1, 2):
            if primes[i / 2]:
                primes[i * i / 2::i] = False
        return int(primes.sum())

#抄来的705ms
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        else:
            prime = [True]*n
            prime[0] = prime[1] =[False]
            for i in range(2,int(math.ceil(math.sqrt(n)+1))):
                if prime[i]:
                    prime[i*i : n :i ] = [False]*len(prime[i*i : n :i ])
            sum = 0
            for i in prime:
                if i == True:
                    sum += 1
            return sum