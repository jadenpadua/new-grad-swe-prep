from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_window = 0
        letter_counts = collections.defaultdict(lambda: 0)
        max_freq_char = 0
        left = 0
        for right in range(len(s)):
            letter_counts[s[right]] += 1
            max_freq_char = max(max_freq_char, letter_counts[s[right]])
            
            while right - left + 1 - max_freq_char > k:
                letter_counts[s[left]] -= 1 
                left += 1
                
            longest_window = max(longest_window, right - left + 1)
            
        return longest_window
