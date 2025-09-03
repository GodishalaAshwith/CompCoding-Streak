from typing import List
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left > right:
            return [-1,-1]

        isPrime = [True]*(right+1)
        isPrime[0] = isPrime[1] = False
        for i in range(2,int(right**0.5)+1):
            if isPrime[i]:
                for j in range(i*i,right+1,i): isPrime[j] = False

        primes = [i for i in range(left,right+1) if isPrime[i]]

        if len(primes) < 2: return [-1,-1]

        minDiff, x,y = float('inf'), -1 , -1
        for i in range(1,len(primes)+1):
            diff = primes[i] - primes[i-1]
            if minDiff < diff:
                minDiff = diff
                x,y = primes[i-1],primes[i]
        return [x,y]