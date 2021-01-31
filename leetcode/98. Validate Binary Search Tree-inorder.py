# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        self.res = []
        return self.inOrder(root)
        
    def inOrder(self, root):
        if not root: return True
        if not self.inOrder(root.left): return False
        if len(self.res) and self.res[-1] >= root.val: return False
        self.res.append(root.val)
        return self.inOrder(root.right)