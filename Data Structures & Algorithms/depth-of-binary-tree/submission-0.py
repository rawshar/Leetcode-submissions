# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue=[]
        res=0
        if not root:
            return res
        queue.append([root])
        while queue:
            level=queue.pop(0)
            res+=1
            temp=[]
            for curr in level:
                if curr.right:
                    temp.append(curr.right)
                if curr.left:
                    temp.append(curr.left)
            if len(temp)>0:
                queue.append(temp)
        return res

        