# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
    
    def helper(self, node, minimum, maximum):
        if node is None:
            return True
        
        if node.val <= minimum or node.val >= maximum:
            return False
        
        leftValid = self.helper(node.left, minimum, node.val)
        rightValid = self.helper(node.right, node.val, maximum)
        
        return leftValid and rightValid
