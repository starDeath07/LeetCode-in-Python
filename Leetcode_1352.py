class ProductOfNumbers:
    def __init__(self):
        self.list = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.list = [1]
            self.size = 0
        else:
            self.list.append(self.list[-1] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if self.size < k:
            return 0

        return self.list[-1] // self.list[-1 - k]
