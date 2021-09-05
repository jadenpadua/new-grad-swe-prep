from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) == 0 or len(t) > len(s):
            return ""
        dct = defaultdict(lambda: 0)
        for char in t:
            dct[char] += 1

        left = 0
        right = 0
        minWindow = len(s) + 1
        output = ""
        counter = len(t)

        while right < len(s):
            if s[right] in dct:
                if dct[s[right]] > 0:
                    counter -= 1
                dct[s[right]] -= 1

            while counter == 0:
                if right - left + 1 < minWindow:
                    minWindow = right - left + 1
                    output = s[left: right+1]

                if s[left] in dct:
                    dct[s[left]] += 1
                    if dct[s[left]] > 0:
                        counter += 1
                        
                left += 1

            right += 1

        return output if minWindow != len(s) + 1 else ""
