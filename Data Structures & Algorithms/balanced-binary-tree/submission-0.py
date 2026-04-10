# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#*******<<<<<<<<<<<< Do Diameter First>>>>>>>>>>>*********
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return 0,True
            else:
                left,val_l=dfs(root.left)
                right,val_r=dfs(root.right)
                val_c= True if abs(left-right)<=1 else False

                return 1+max(left,right), True if val_c and val_l and val_r else False
        height,val = dfs(root)
        return val

        