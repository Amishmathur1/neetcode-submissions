# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        def sameTree(s, t):
            if s is None and t is None:
                return True
            if s and t and s.val == t.val:
                return sameTree(s.left, t.left) and sameTree(s.right, t.right)
            
            return False

        if t is None:   return True
        if s is None:   return False

        if sameTree(s,t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

        