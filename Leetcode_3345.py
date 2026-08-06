class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def get_prod(x: int) -> int:
            curr = 1
            while x:
                curr = curr * (x % 10)
                x //= 10
            return curr

        while True:
            num = get_prod(n)
            if num % t == 0:
                break
            n += 1
        return n
