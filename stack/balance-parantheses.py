class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = list(s)
        stack = []
        for i in range(len(arr)):
            if arr[i] == "(":
                stack.append(i)    
            elif arr[i] == ")":
                if stack:
                    stack.pop()
                else:
                    arr[i] = ''
        while stack:
            arr[stack.pop()] = ''
        
        return ''.join(arr)
