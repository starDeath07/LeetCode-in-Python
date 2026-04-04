class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        n = len(encodedText)
        cols = n // rows
        ans: list[str] = []

        for i in range(cols):
            j = i
            while j < n:
                ans.append(encodedText[j])
                j += cols + 1

        return "".join(ans).rstrip()
