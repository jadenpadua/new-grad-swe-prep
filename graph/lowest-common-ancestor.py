# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # keep jumping to parents until dist is 0
        def jumpToParent(u, dist):
            while dist > 0:
                u = parent_map[u]
                dist -= 1
            return u
        # dfs to find level and parent map
        def dfs(u, p, level):
            if u == None: return
            parent_map[u] = p
            level_map[u] = level
            dfs(u.left, u, level + 1)
            dfs(u.right, u, level + 1)
            
        parent_map = {}
        level_map = {}
        dfs(root, None, 0)
        # Level the nodes
        if level_map[p] < level_map[q]:
            q = jumpToParent(q, level_map[q] - level_map[p])
        else:
            p = jumpToParent(p, level_map[p] - level_map[q])
        # Since they are leveled keep moving up to recurse to LCA
        while q != p:
            q = parent_map[q]
            p = parent_map[p]
        return q
