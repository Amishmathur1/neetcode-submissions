# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traversal(root, x):
            if root is None:
                x.append("x")
                return 
            x.append(root.val)
            traversal(root.left, x)
            traversal(root.right, x)

            return x
        
        l1, l2 = [], []
        l1 = traversal(p, l1)
        l2 = traversal(q, l2)
        return l1==l2