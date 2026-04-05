class Solution:
    def judgeCircle(self, moves: str) -> bool:
        n = len(moves)
        x, y = 0, 0

        for c in moves:
            if c == "L":
                x -= 1
            elif c == "R":
                x += 1
            elif c == "U":
                y += 1
            else:
                y -= 1

        return x == 0 and y == 0
