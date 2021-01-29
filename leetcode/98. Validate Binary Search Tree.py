class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = [(root, -float('inf'), float('inf'))]
        while len(stack):
            node, lower, upper = stack.pop()
            if node.val <= lower or node.val >= upper:
                return False
            if node.left:
                stack.append([node.left, lower, node.val])
            if node.right:
                stack.append([node.right, node.val, upper])
        return True