class Solution:
    def findPrimePairs(self, n: int) -> list[list[int]]:
        is_prime: list[bool] = [True] * (n + 1)

        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        ans: list[list[int]] = []

        for i in range(2, n + 1):
            if is_prime[i] and is_prime[n - i]:
                ans.append([i, n - i])
                is_prime[i] = False

        return ans
