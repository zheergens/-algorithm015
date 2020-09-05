# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        def helper(root: TreeNode):
            if root:
                helper(root.left)
                helper(root.right)
                res.append(root.val)
        helper(root)
        return res