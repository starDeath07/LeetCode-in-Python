from typing import List, Set


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        self.mat: List[List[int]] = mat
        self.m: int = len(mat)
        self.n: int = len(mat[0])
        self.target: int = target

        achievable: Set[int] = {0}  # sums achievable so far

        for row in self.mat:
            new_achievable: Set[int] = set()
            for s in achievable:
                for val in row:
                    new_achievable.add(s + val)
            achievable = new_achievable

        # Find the sum closest to the target
        result: int = min(abs(self.target - s) for s in achievable)
        return result

