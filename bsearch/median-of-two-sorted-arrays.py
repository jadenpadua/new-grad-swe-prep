class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        # Gurantee that A is the smaller array
        if len(A) > len(B):
            A, B = B, A
        
        left, right = 0, len(A) - 1
        # Guranteed there will be a median
        while True:
            i = (left + right) // 2 # A ptr
            j = half - i - 2 # B ptr, account for indeces of A and B arr
            
            ALeft = A[i] if i >= 0 else float("-inf")
            ARight = A[i+1] if (i + 1) < len(A) else float("inf")
            BLeft = B[j] if j >= 0 else float("-inf")
            BRight = B[j+1] if (j + 1) < len(B) else float("inf")
            
            # Median is found
            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 1:
                    return min(ARight, BRight)
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            # reduce size of A partition
            elif ALeft > BRight:
                right = i - 1
            # increase size of A partition
            else:
                left = i + 1
