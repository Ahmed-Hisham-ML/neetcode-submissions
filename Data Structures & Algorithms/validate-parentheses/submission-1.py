from collections import deque

class Solution:

    def isValid(self, s: str) -> bool:
        stack = deque()

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for character in s:

            if character in ["(", "{", "["]:
                stack.append(character)

            else:
                if not stack:
                    return False

                if stack[-1] == pairs[character]:
                    stack.pop()
                else:
                    return False

        return not stack