class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        res = 0
        for right in range(len(s)):
            if s[right] not in seen:
                res = max(res, right - left + 1)
            else:
                if seen[s[right]] >= left:
                    left = seen[s[right]] + 1
                else:
                    res = max(res, right - left + 1)
            seen[s[right]] = right
        return res
