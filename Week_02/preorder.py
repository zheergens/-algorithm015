"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = list()
        def helper(root: 'Node'):
            if root:
                res.append(root.val)
                for child in root.children:
                    helper(child)
        helper(root)
        return res