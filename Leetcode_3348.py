class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        n = len(num)
        temp = t

        for i in [2, 3, 5, 7]:
            while temp % i == 0:
                temp //= i

        if temp != 1:
            return "-1"

        zero_pos = n - 1
        remaining_factor = [t]

        for i in range(n):
            digit = ord(num[i]) - ord("0")
            if digit == 0:
                zero_pos = i
                break

            factor = remaining_factor[-1] // self.gcd(remaining_factor[-1], digit)
            remaining_factor.append(factor)

        if len(remaining_factor) == n + 1 and remaining_factor[-1] == 1:
            return num

        for index in range(zero_pos, -1, -1):
            req_factor = remaining_factor[index]
            free_slots = n - 1 - index
            value = ord(num[index]) - ord("0") + 1

            for digit in range(value, 10):
                next_req_factor = req_factor // self.gcd(req_factor, digit)
                req_num = self.slots_filler(next_req_factor, free_slots)

                if len(req_num) == free_slots:
                    return num[0:index] + str(digit) + req_num

        return self.slots_filler(t, n + 1)

    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def slots_filler(self, required: int, length: int) -> str:
        arr: list[int] = []

        for i in range(9, 1, -1):
            while required % i == 0:
                arr.append(i)
                required //= i

        while len(arr) < length:
            arr.append(1)

        arr.reverse()
        return "".join(map(str, arr))
