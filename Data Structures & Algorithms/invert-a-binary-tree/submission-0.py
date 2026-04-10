# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack=[]
        head=root
        stack.append(root)
        while stack:
            curr=stack.pop()
            print(curr.val)
            left=curr.left
            right=curr.right
            if left:
                stack.append(left)
            if right:
                stack.append(right)
            temp=left
            curr.left=right
            curr.right=temp
        return head
        