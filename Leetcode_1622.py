class Fancy:
    def __init__(self) -> None:
        self.values: list[int] = []
        self.add: int = 0
        self.mult: int = 1
        self.MOD: int = 10**9 + 7

    def append(self, val: int) -> None:
        curr: int = (val - self.add + self.MOD) % self.MOD
        curr = curr * self.fast_power(self.mult % self.MOD, self.MOD - 2)
        self.values.append(curr)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.add = (self.add * m) % self.MOD
        self.mult = (self.mult * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        return (
            -1
            if idx >= len(self.values)
            else (self.values[idx] * self.mult % self.MOD + self.add) % self.MOD
        )

    def fast_power(self, a: int, b: int) -> int:
        result = 1

        while b > 0:
            if (b & 1) == 1:
                result *= a % self.MOD
            a = a * a % self.MOD
            b >>= 1
        return result
