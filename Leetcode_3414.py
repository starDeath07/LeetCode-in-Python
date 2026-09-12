from functools import cache


class Solution:
    class Node:
        def __init__(self) -> None:
            self.score: int = 0
            self.arr: list[int] = []

    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)

        for i in range(n):
            intervals[i].append(i)

        intervals.sort(key=lambda x: x[0])

        self.intervals = intervals
        self.next_index = [0] * n

        for i in range(n):
            self.next_index[i] = self.nextIndex(intervals, intervals[i][1])

        return self.finder(0, 4).arr

    @cache
    def finder(self, i: int, k: int):
        if i >= len(self.intervals) or k == 0:
            return self.Node()

        skip = self.finder(i + 1, k)

        wt = self.intervals[i][2]
        original_index = self.intervals[i][3]
        j = self.next_index[i]

        temp = self.finder(j, k - 1)

        take = self.Node()
        take.score = temp.score + wt

        # IMPORTANT: make a copy
        take.arr = temp.arr.copy()
        take.arr.append(original_index)
        take.arr.sort()

        if skip.score > take.score:
            return skip

        if take.score > skip.score:
            return take

        # Same score -> lexicographically smaller indices
        return take if take.arr < skip.arr else skip

    def nextIndex(self, intervals: list[list[int]], end: int) -> int:
        left = 0
        right = len(intervals) - 1
        index = len(intervals)

        while left <= right:
            mid = left + (right - left) // 2

            if intervals[mid][0] > end:
                index = mid
                right = mid - 1
            else:
                left = mid + 1

        return index
