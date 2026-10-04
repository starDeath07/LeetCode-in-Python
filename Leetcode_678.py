class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        stack: list[int] = []
        extra: list[int] = []

        for i in range(n):
            if s[i] == "*":
                extra.append(i)
            elif s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif extra:
                    extra.pop()
                else:
                    return False

        while stack and extra:
            if stack.pop() > extra.pop():
                return False

        return len(stack) == 0
