from itertools import pairwise
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def inorder(self, root, result):
        if not root:
            return []
        left = self.inorder(root.left, result)
        val = [root.val]
        right = self.inorder(root.right, result)
        return left + val + right

    def isValidBST(self, root: TreeNode | None) -> bool:
        result = self.inorder(root, [])
        sorted_result = result.copy()
        sorted_result.sort()

        return sorted_result == result and all(a < b for a, b in pairwise(result))
        
        
        
        


        