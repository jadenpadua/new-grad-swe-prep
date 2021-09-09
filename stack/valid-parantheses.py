class Solution:
    def isValid(self, s: str) -> bool:
        ht = {")":"(", "}":"{", "]":"["}
        stack = []
        opening= "({["
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                toppedChar = stack.pop()
                if toppedChar != ht[char]:
                    return False
        return len(stack) == 0
