class Solution:
    def countPrimes(self, n: int) -> int:
        def sieve(n):
            primes = [True] * n
            p = 2

            while p * p <= n:
                if primes[p]:
                    for i in range(p * p, n, p):
                        primes[i] = False
                p += 1
            
            return [p for p in range(2, n) if primes[p]]

        primes = sieve(n)
        return len(primes)