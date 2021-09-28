# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # First idx stores diameter, second stores height
        res = [0, 0]
        
        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            # adding two everytime to account for the 2 edges going out of the node
            nodeDiameter = left + right + 2
            res[0] = max(res[0], nodeDiameter)
            # Return nodes max height, adding one to account for the node itself
            return 1 + max(left, right)
        
        dfs(root)
        return res[0]
