class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        freq_even: list[int] = [0] * 26
        freq_odd: list[int] = [0] * 26

        for i in range(n):
            index1 = ord(s1[i]) - ord("a")
            index2 = ord(s2[i]) - ord("a")
            if i % 2 == 0:
                freq_even[index1] += 1
                freq_even[index2] -= 1
            else:
                freq_odd[index1] += 1
                freq_odd[index2] -= 1

        for i in range(26):
            if freq_odd[i] > 0 or freq_even[i] > 0:
                return False

        return True
