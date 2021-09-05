from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
    
        t_letter_map = defaultdict(lambda: 0)
        s_letter_map = defaultdict(lambda: 0)
        
        for i in range(len(t)):
            t_letter_map[t[i]] += 1
            s_letter_map[s[i]] += 1
        
        return t_letter_map == s_letter_map
