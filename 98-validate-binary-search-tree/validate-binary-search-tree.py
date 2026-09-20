from itertools import pairwise
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def inorder(self, root, result):
        valid = True
        if not root:
            return valid, []
        valid_left, left = self.inorder(root.left, result)
        val = [root.val]
        valid_right, right = self.inorder(root.right, result)
        if (left and left[-1] == val[0]) or (right and right[0] == val[0]) or (not valid_left) or (not valid_right):
            valid = False
        out = left + val + right
        return valid, out

    def isValidBST(self, root: TreeNode | None) -> bool:
        valid, result = self.inorder(root, [])
        sorted_result = result.copy()
        sorted_result.sort()
        return valid and sorted_result == result
        
        
        
        


        