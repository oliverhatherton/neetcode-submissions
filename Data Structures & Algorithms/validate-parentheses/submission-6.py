class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "}": "{", "]": "["}
        stack = []

        parenthesis = list(s)

        for char in parenthesis:
            if char in pairs.values():
                stack.append(char)
            else:
                if len(stack) < 1 or stack[-1] != pairs[char]:
                    return False
                stack.pop()

        return len(stack) == 0