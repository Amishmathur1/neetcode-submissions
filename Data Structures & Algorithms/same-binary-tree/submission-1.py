# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inord(root, x):
            if root is None:
                x.append('x')
                return 
            
            x.append(root.val)
            inord(root.left, x)
            
            inord(root.right, x)
            return x
        nums = []
        nums2 = []
        l1 = inord(p, nums)
        l2 = inord(q, nums2)
        return l1 == l2
