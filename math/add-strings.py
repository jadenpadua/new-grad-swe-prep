class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        nums1, nums2 = list(num1), list(num2)
        carry = 0
        res = []
        
        while len(nums1) > 0 or len(nums2) > 0:
            n1, n2 = 0, 0
            if len(nums1) > 0:
                n1 = ord(nums1.pop()) - ord('0')
            if len(nums2) > 0:
                n2 = ord(nums2.pop()) - ord('0')
            
            temp = n1 + n2 + carry
            res.append(temp % 10)
            carry = temp // 10
        
        if carry:
            res.append(carry)
        
        return ''.join([str(i) for i in res])[::-1]
