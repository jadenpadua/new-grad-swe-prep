# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
    
        level_order = []
        queue = deque([root])
        
        while len(queue) != 0:
            level_len = len(queue)
            level_nodes = []
            for i in range(level_len):
                curr_node = queue.popleft()
                level_nodes.append(curr_node.val)
                
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            
            level_order.append(level_nodes)
        
        return level_order
