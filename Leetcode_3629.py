from collections import defaultdict, deque
from typing import Dict, List, Set, Deque


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        maxi = max(nums)

        mp: Dict[int, List[int]] = defaultdict(list)

        for i in range(n):
            mp[nums[i]].append(i)

        is_prime: List[bool] = self.get_primes(maxi)

        is_visited: List[bool] = [False] * n
        seen: Set[int] = set()

        q: Deque[int] = deque([0])
        is_visited[0] = True

        while q:
            size = len(q)

            for _ in range(size):
                index = q.popleft()

                if index == n - 1:
                    return ans

                # move right
                if index + 1 < n and not is_visited[index + 1]:
                    q.append(index + 1)
                    is_visited[index + 1] = True

                # move left
                if index - 1 >= 0 and not is_visited[index - 1]:
                    q.append(index - 1)
                    is_visited[index - 1] = True

                # prime jumps
                if is_prime[nums[index]] and nums[index] not in seen:
                    seen.add(nums[index])

                    mult = nums[index]

                    while mult <= maxi:
                        if mult in mp:
                            for nxt in mp[mult]:
                                if not is_visited[nxt]:
                                    q.append(nxt)
                                    is_visited[nxt] = True

                        mult += nums[index]

            ans += 1

        return -1

    def get_primes(self, n: int) -> List[bool]:
        is_prime: List[bool] = [True] * (n + 1)

        if n >= 0:
            is_prime[0] = False

        if n >= 1:
            is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        return is_prime
